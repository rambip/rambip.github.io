class MarimoMermaid extends HTMLElement {
  constructor() {
    super();
    this._id = this._randomAlpha();
    this._diagram = "";
    this._darkMode = false;
  }

  static get observedAttributes() {
    return ["data-diagram", "dark-mode"];
  }

  connectedCallback() {
    this._updateDiagram();
    this._render();
  }

  attributeChangedCallback(name, oldValue, newValue) {
    if (oldValue === newValue) return;

    if (name === "data-diagram") {
      this._updateDiagram();
    } else if (name === "dark-mode") {
      this._darkMode = newValue === "true";
    }

    if (this.isConnected) {
      this._render();
    }
  }

  _updateDiagram() {
    const raw = this.getAttribute("data-diagram") || "";

    // The attribute value is a JSON-encoded string
    try {
      this._diagram = JSON.parse(raw);
    } catch {
      // Fallback: use as-is
      this._diagram = raw;
    }
  }

  _randomAlpha() {
    const alphabet = "abcdefghijklmnopqrstuvwxyz";
    return Array.from(
      { length: 6 },
      () => alphabet[Math.floor(Math.random() * alphabet.length)],
    ).join("");
  }

  async _render() {
    if (!this._diagram) {
      this.innerHTML = "";
      return;
    }

    const config = {
      startOnLoad: true,
      theme: this._darkMode ? "dark" : "forest",
      darkMode: this._darkMode,
      logLevel: "fatal",
      securityLevel: "strict",
      fontFamily: "var(--text-font)",
      arrowMarkerAbsolute: false,
      flowchart: {
        htmlLabels: true,
        curve: "linear",
      },
      sequence: {
        diagramMarginX: 50,
        diagramMarginY: 10,
        actorMargin: 50,
        width: 150,
        height: 65,
        boxMargin: 10,
        boxTextMargin: 5,
        noteMargin: 10,
        messageMargin: 35,
        mirrorActors: true,
        bottomMarginAdj: 1,
        useMaxWidth: true,
        rightAngles: false,
        showSequenceNumbers: false,
      },
      gantt: {
        titleTopMargin: 25,
        barHeight: 20,
        barGap: 4,
        topPadding: 50,
        leftPadding: 75,
        gridLineStartPadding: 35,
        fontSize: 11,
        numberSectionStyles: 4,
        axisFormat: "%Y-%m-%d",
      },
    };

    if (typeof mermaid !== "undefined") {
      mermaid.initialize(config);

      try {
        const result = await mermaid.render(this._id, this._diagram, undefined);
        this.innerHTML = result.svg;
      } catch (error) {
        document.getElementById(this._id)?.remove();
        console.warn("Failed to render mermaid diagram", error);
        this.innerHTML = "";
      }
    } else {
      console.error("Mermaid library not loaded");
    }
  }
}

customElements.define("marimo-mermaid", MarimoMermaid);
class MarimoTex extends HTMLElement {
  connectedCallback() {
    // Wait for content to be available
    setTimeout(() => {
      const latex = this.textContent.slice(3, -3);
      if (!latex) return;

      this.innerHTML = "";
      katex.render(latex, this, {
        throwOnError: false,
        displayMode: this.hasAttribute("display"),
      });
    }, 0);
  }
}

customElements.define("marimo-tex", MarimoTex);
