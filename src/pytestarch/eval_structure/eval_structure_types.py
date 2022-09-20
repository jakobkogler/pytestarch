"""Abstract types to specify the interface of evaluable objects."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Optional, Any, Set

from pytestarch.eval_structure.graph import Node


class Evaluable(Protocol):
    def is_dependent(self, dependent: Module, dependent_upon: Module) -> bool:
        """Returns True if the dependent module is indeed
        depending on the dependent_upon module.
        Submodules of dependent towards are taken into account, but submodules of dependent_upon are not.

        Args:
            dependent: Module
            dependent_upon: Module

        Returns:
            Indicator of whether the dependent module truly depends on the dependent_upon module
        """
        raise NotImplementedError()

    def any_dependency_to_module_other_than(
        self, dependent: Module, dependent_upon: Module
    ) -> Set[Module]:
        """Returns True if the dependent module has any
        dependency to a module other than the dependent_upon module
        or any of its submodules.

        Args:
            dependent: Module
            dependent_upon: Module

        Returns:
            All modules other than dependent_upon on which dependent module as any dependency
        """
        raise NotImplementedError()

    def any_dependency_to_other_module_than(
        self, dependent: Module, dependent_upon: Module
    ) -> Set[Module]:
        """Returns True if any module other than the dependent
        module and its submodules has any dependency to the
        dependent_upon module.

        Args:
            dependent: Module
            dependent_upon: Module

        Returns:
            All modules other than dependent that have any dependency on the dependent upon module
        """
        raise NotImplementedError()

    def visualize(self, **kwargs: Any) -> None:
        """Uses matplotlib to draw the underlying dependency structure.

        Args:
            **kwargs: Any formatting options available for networkx' drawing function, as this is currently the only
                available backend.
                Exception: If 'spacing' is set, this will be interpreted as the parameter 'k' of the spring layout (https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html#networkx.drawing.layout.spring_layout).
        """
        raise NotImplementedError()


@dataclass(frozen=True)
class Module:
    """Represents a python module.
    The module can either be identified by its name or by the name of a parent module.

    Attributes:
        name: full name of the module
        parent_module: full name of the parent module
    """

    name: Optional[str] = None
    parent_module: Optional[Node] = None