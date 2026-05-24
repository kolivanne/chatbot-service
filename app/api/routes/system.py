from fastapi import APIRouter

router = APIRouter(tags=["system"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """
    Health-Check-Endpunkt für Monitoring- und
    Orchestrierungs-Systeme wie Kubernetes.

    Kann für Liveness- oder Readiness-Probes
    verwendet werden.
    """
    return {"status": "ok"}