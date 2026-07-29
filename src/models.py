from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Task:

    texto: str
    completada: bool = False

    def to_dict(self) -> dict:

        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":

        return cls(
            texto=data.get("texto", ""),
            completada=data.get("completada", False),
        )

    def __str__(self) -> str:

        estado = "✅" if self.completada else "❌"
        return f"[{estado}] {self.texto}"
