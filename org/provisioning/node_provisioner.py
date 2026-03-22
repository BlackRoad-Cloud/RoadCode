"""Node provisioner — spin up new fleet nodes."""
from dataclasses import dataclass
from enum import Enum

class NodeType(Enum):
    PI = "raspberry-pi"
    DROPLET = "digitalocean"
    LOCAL = "local-docker"

@dataclass
class NodeSpec:
    name: str
    type: NodeType
    region: str = "local"
    ram_gb: int = 4
    storage_gb: int = 64
    services: list[str] = None

    def __post_init__(self):
        self.services = self.services or []

class Provisioner:
    async def create(self, spec: NodeSpec) -> dict:
        if spec.type == NodeType.DROPLET:
            return {"status": "created", "provider": "digitalocean", "name": spec.name}
        elif spec.type == NodeType.PI:
            return {"status": "ready", "provider": "local", "name": spec.name}
        return {"status": "unknown"}
