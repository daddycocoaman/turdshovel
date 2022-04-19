from typing import List, Tuple

from rich.console import RenderableType
from rich.json import JSON
from rich.traceback import Traceback
from textual.widgets import TreeClick, TreeControl

from ..parsing import parse_obj

AssemblyInstances = List[Tuple[str, str]]


class TurdshovelTreeControl(TreeControl):
    def render(self) -> RenderableType:
        self._tree.style = "#c59b00"
        self._tree.guide_style = "#9e0700"
        return self._tree


class AssemblyTree(TurdshovelTreeControl):
    async def handle_tree_click(self, message: TreeClick):
        runtime = self.app.runtime
        if runtime:
            self.app.assembly_instances_list = AssemblyInstanceTree(
                message.node.data, data=[], name=self.app.assembly_instances_list.name
            )
            for segment in runtime.Heap.Segments:
                for obj in segment.EnumerateObjects():
                    if (
                        obj.IsValid
                        and not obj.IsFree
                        and str(obj.Type) == message.node.data
                    ):
                        await self.app.assembly_instances_list.add(
                            self.app.assembly_instances_list.root.id,
                            hex(obj.Address),
                            obj.Address,
                        )

            await self.app.assembly_instances_list.root.expand()
            await self.app.assembly_instances_view.update(
                self.app.assembly_instances_list
            )
            self.app.assembly_instances_view.refresh(layout=True)


class AssemblyInstanceTree(TurdshovelTreeControl):
    async def handle_tree_click(self, message: TreeClick):
        runtime = self.app.runtime
        if runtime:
            try:
                address = int(message.node.data)
                obj = runtime.Heap.GetObject(address)

                # We only care about valid objects and non-Free objects
                if obj.IsValid and not obj.IsFree:
                    if obj.IsArray:
                        output = []
                        obj_list = obj.AsArray()
                        for idx in range(0, obj_list.Length):
                            item = obj_list.GetObjectValue(idx)
                            if not item.IsNull:
                                output.append(parse_obj(runtime, item))
                    else:
                        output = parse_obj(runtime, obj)

                output = JSON.from_data(output, check_circular=False)
            except:
                output = Traceback(theme="monokai", width=None, show_locals=True)

        await self.app.dumpview.update(output)
