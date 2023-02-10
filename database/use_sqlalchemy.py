from sqlalchemy import Column, create_engine, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm.collections import attribute_mapped_collection

Base = declarative_base()


class TreeNode():  # (Base):
    #__tablename__ = "tree"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey(id))
    name = Column(String(50), nullable=False)

    children = relationship(
        "TreeNode",
        # cascade deletions
        cascade="all, delete-orphan",
        # many to one + adjacency list - remote_side
        # is required to reference the 'remote'
        # column in the join condition.
        backref=backref("parent", remote_side=id),
        # children will be represented as a dictionary
        # on the "name" attribute.
        collection_class=attribute_mapped_collection("name"),
    )

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __repr__(self):
        return "TreeNode(name=%r, id=%r, parent_id=%r)" % (
            self.name,
            self.id,
            self.parent_id,
        )

    def dump(self, _indent=0):
        return (
            "   " * _indent
            + repr(self)
            + "\n"
            + "".join([c.dump(_indent + 1) for c in self.children.values()])
        )


def example_tree_table_no_rdbms(session: Session):
    "Creating Tree Table"
    node = TreeNode("rootnode")
    TreeNode("node1", parent=node)
    TreeNode("node3", parent=node)

    node2 = TreeNode("node2")
    TreeNode("subnode1", parent=node2)
    node.children["node2"] = node2
    TreeNode("subnode2", parent=node.children["node2"])

    print(f"Created new tree structure:\n{node.dump()}")
    session.add(node)
    session.commit()

    print(f"Tree After Save:\n{node.dump()}")
    TreeNode("node4", parent=node)
    TreeNode("subnode3", parent=node.children["node4"])
    TreeNode("subnode4", parent=node.children["node4"])
    TreeNode("subsubnode1", parent=node.children["node4"].children["subnode3"])

    # remove node1 from the parent, which will trigger a delete
    # via the delete-orphan cascade.
    del node.children["node1"]
    print("Removed node1.  flush + commit:")
    session.commit()

    # query
    session.expunge_all()
    node = (
        session.query(TreeNode)
        .options(
            joinedload("children")
            .joinedload("children")
            .joinedload("children")
            .joinedload("children")
        )
        .filter(TreeNode.name == "rootnode")
        .first()
    )
    print("Full Tree:\n%s" % node.dump())


class simNode(Base):
    "Custom table structure"
    __tablename__ = "hrh_sim_tbl"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    details = Column(String(150), nullable=False)
    note = Column(String(150))

    def __init__(self, name, details="void str, warning!", note=None):
        self.name = name
        self.details = details
        self.note = note

    def __repr__(self):
        return "simNode(id={}, name={}, details={})\n".format(self.id, self.name, self.details)

    def __str__(self) -> str:
        return self.__repr__()


if __name__ == "__main__":
    def msg(msg: str):
        print("\n\n" + "-" * len(msg.split("\n")[0]))
        print(msg)
        print("-" * len(msg.split("\n")[0]))

    mysql_addr = {"host": "127.0.0.1", "user": "root",
                  "password": "123456", "dbname": "amust_demo"}
    engine = create_engine(
        'mysql+mysqlconnector://{user}:{password}@{host}/{dbname}'.format(**mysql_addr), pool_recycle=3600)

    Base.metadata.create_all(engine)
    session = Session(engine)

    nodes = [
        simNode("risk",),
        # simNode("KKK2", details="KKK record!"),
    ]

    msg(f"Creating:\n{nodes}")
    session.add_all(nodes)
    session.commit()

    # msg("flush + commit:")
    # msg("After Save:\n %s", node.dump())
    # msg("Tree after save:\n %s", node.dump())

    session.close()
