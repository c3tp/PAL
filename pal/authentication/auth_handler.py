from abc import ABC, abstractmethod


class AbstractOperation(ABC):

    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()

    @abstractmethod
    def execute(self):
        pass


class AddOperation(AbstractOperation):
    def execute(self):
        return self.operand_a + self.operand_b


def do_some_adding(first_operand, second_operand):
    add_op = AddOperation(first_operand, second_operand)
    return add_op.execute()
