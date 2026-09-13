import { useEffect, useState } from "react";

const measures = [
  { label: "Qualite geometrie", value: "94%", confidence: 94 },
  { label: "Facial width / height", value: "0.667", confidence: 92 },
  { label: "Canthal tilt gauche", value: "+6.5 deg", confidence: 98 },
  { label: "Canthal tilt droit", value: "+6.5 deg", confidence: 98 },
];

export function App() {
  const [engineOnline, setEngineOnline] = useState<boolean | null>(null);

  useEffect(() => {
    const apiUrl = import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8765";
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 2500);

    fetch(`${apiUrl}/health`, { signal: controller.signal })
      .then((response) => setEngineOnline(response.ok))
      .catch(() => setEngineOnline(false))
      .finally(() => window.clearTimeout(timeout));

    return () => {
      window.clearTimeout(timeout);
      controller.abort();
    };
  }, []);

  return (
    <main className="shell">
      <header>
        <div>
          <p className="eyebrow">LOCAL MORPHOMETRY ENGINE</p>
          <h1>VisageQuant</h1>
        </div>
        <div className="status-group">
          <span className={`engine-pill ${engineOnline ? "online" : ""}`}>
            <i />
            {engineOnline === null ? "moteur..." : engineOnline ? "moteur actif" : "moteur hors ligne"}
          </span>
          <span className="local-pill">100% local</span>
        </div>
      </header>

      <section className="hero-panel">
        <div className="scan-placeholder" aria-label="Zone du futur scan facial">
          <div className="face-guide" />
          <span>Acquisition non connectee</span>
        </div>
        <div className="intro">
          <p className="step">ETAPE 01 / ACQUISITION</p>
          <h2>Construire une mesure fiable avant de construire un score.</h2>
          <p>
            Le socle controle la qualite, refuse les donnees insuffisantes et conserve la
            provenance de chaque resultat.
          </p>
          <button type="button" disabled>
            Demarrer un scan — bientot
          </button>
        </div>
      </section>

      <section className="results">
        <div className="section-title">
          <div>
            <p className="eyebrow">DONNEES SYNTHETIQUES</p>
            <h2>Pipeline de demonstration</h2>
          </div>
          <strong>v0.1.0</strong>
        </div>
        <div className="measure-grid">
          {measures.map((measure) => (
            <article key={measure.label}>
              <span>{measure.label}</span>
              <strong>{measure.value}</strong>
              <div className="bar"><i style={{ width: `${measure.confidence}%` }} /></div>
              <small>Confiance {measure.confidence}%</small>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
