import { cleanup, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { App } from "./App";

afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
});

describe("engine status", () => {
  it("shows that the local engine is available after a successful health check", async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true });
    vi.stubGlobal("fetch", fetchMock);

    render(<App />);

    expect(await screen.findByText("moteur actif")).toBeInTheDocument();
    expect(fetchMock).toHaveBeenCalledWith(
      "http://127.0.0.1:8765/health",
      expect.objectContaining({ signal: expect.any(AbortSignal) }),
    );
  });

  it("reports an unavailable engine when the health check fails", async () => {
    vi.stubGlobal("fetch", vi.fn().mockRejectedValue(new Error("offline")));

    render(<App />);

    expect(await screen.findByText("moteur hors ligne")).toBeInTheDocument();
  });
});
