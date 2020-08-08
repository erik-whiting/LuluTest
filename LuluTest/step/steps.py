from LuluTest.element import BaseElement
from .step import Step


class Steps:
    def __init__(self, action_object, step_builders):
        self.action_object = action_object
        self.each = []
        for builder in step_builders:
            self.each.append(self.__resolve_step(builder))

    def __resolve_step(self, step):
        if isinstance(step, BaseElement):
            return step

        resolved_step = None
        if len(step) == 2:
            resolved_step = Step(
                action_object=self.action_object,
                operation=step[0],
                subject=step[1]
            )
        elif len(step) == 3:
            resolved_step = Step(
                action_object=self.action_object,
                operation=step[0],
                subject=step[1],
                data=step[2]
            )
        return resolved_step
