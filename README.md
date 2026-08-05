<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1020,50:5B21B6,100:06B6D4&height=210&section=header&text=Hey,%20I'm%20Luna&fontSize=46&fontColor=E5E7EB&fontAlignY=42&desc=I%20build%20systems%20that%20are%20supposed%20to%20be%20toys%20and%20refuse%20to%20stay%20that%20way&descSize=16&descAlignY=62&animation=fadeIn" alt="header" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&duration=2800&pause=900&color=A78BFA&center=true&vCenter=true&width=650&lines=full-stack+dev+%2B+systems+programmer;building+MahinaOS+from+the+kernel+up;shipping+multi-agent+AI+platforms;documentation-first%2C+always" alt="typing"/>

<br/>

<img src="https://img.shields.io/badge/focus-AI_agents_·_systems_·_web-06B6D4?style=for-the-badge&labelColor=0B1020"/>
<img src="https://img.shields.io/badge/mode-dark_only-5B21B6?style=for-the-badge&labelColor=0B1020"/>
<img src="https://img.shields.io/badge/philosophy-docs_before_code-E5E7EB?style=for-the-badge&labelColor=0B1020"/>

</div>

<br/>

## What this profile actually is

Most of what's public here is coursework — a long tail of small class exercises. This README isn't about that tail. It's about the handful of repos where I decided a weekend project should behave like a real product: hackathon platforms with real architecture diagrams, a Linux distro built from a documentation spec instead of vibes, and a personal AI stack that's been through seven versions.

If a project below doesn't have a live badge, it's because it's a prototype and I'd rather say that than fake a demo link.

<br/>

## Flagship builds

<table>
<tr>
<td width="50%" valign="top">

### 🛡️ [AEGIS — Decision Intelligence Platform](https://github.com/HardikBhaskar2010/AEGIS-Decision-Intelligence-Platform)

Built for **Google Cloud's Gen AI Academy (APAC)** hackathon with Hack2Skill. Turns fragmented city-ops data (transit, weather, utilities, citizen feedback) into an explainable, cited "Situation Brief" instead of five open dashboards.

A 5-agent graph (Orchestrator → Query → Correlation → Forecast → Narrative) runs on **ADK 2.0** over **BigQuery**, streamed live to a **React Flow** agent-graph visualization so you can watch the reasoning happen, not just the output.

`React · FastAPI · BigQuery · Firestore · Gemini 3 · MapLibre`

</td>
<td width="50%" valign="top">

### 🧠 [SMRITI — Knowledge Debt Intelligence](https://github.com/HardikBhaskar2010/SMRITI-Smart-Maintenance-Retrieval-Intelligence-)

Selected for **Phase 2** of the Economic Times AI Hackathon. Industrial plants lose decades of unwritten technician knowledge when experts leave — SMRITI quantifies that loss as a score, forecasts which assets go critical, and flags experts at flight risk before they walk out the door.

Phase 2 added streaming Gemini 2.0 Flash responses, JWT role-based auth, and a React-Three-Fiber 3D knowledge graph on top of the original RAG core.

`FastAPI · React · Gemini · WebSockets · R3F`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌙 [MahinaOS](https://github.com/HardikBhaskar2010/MahinaOS)

Not a themed Linux install — an actual from-scratch OS: custom PID-1 init (`luna-init`, TOML service graphs, cycle detection), a malloc-free boot splash writing directly to the framebuffer, a custom display protocol (**LGP**), and a native C17 GUI toolkit. All of it written *after* the architecture was documented, not before.

Currently in Phase 3 — compositor, shell, and ten desktop apps running under QEMU.

`C17 · Linux kernel · Limine · Makefile/QEMU`

</td>
<td width="50%" valign="top">

### 🤖 [Veronica — Sovereign AI](https://github.com/HardikBhaskar2010/Veronica-v7-main)

A private AI that isn't a chat wrapper: system-level perception (active window, clipboard, cursor focus on Windows), Whisper speech-to-text, BLIP vision, and a persistent memory graph that maps real contacts across WhatsApp and email. Hybrid brain — local via Ollama, or scales out to Gemini/Claude for harder reasoning.

Now at **v7.2**, seven iterations deep on the same long-term thesis.

`FastAPI · Ollama · Gemini/Claude API · Whisper · BLIP`

</td>
</tr>
</table>

<div align="center">

**🎬 [Sunad OTT](https://github.com/HardikBhaskar2010/OTT)** — a bilingual (Hindi/English) streaming platform for Indian civilizational storytelling. Next.js 14 frontend on Vercel's edge network, a separate Express/TypeScript API on Render, Firebase auth + Firestore, Razorpay webhooks — a real split-service architecture, not a single monorepo demo.

</div>

<br/>

## How I actually work

- **Documentation before code.** MahinaOS has a six-volume internal spec (the "Divine Collection of Knowledge") that the code has to satisfy — if it's not written down first, it doesn't get built.
- **Architecture diagrams aren't decoration.** AEGIS ships with real Mermaid sequence diagrams and an ERD because I use them to think, not just to explain afterward.
- **I say when something's a prototype.** AEGIS's own README leads with a warning that it runs on mock data. I'd rather be accurate than impressive.
- **Iterate in public version numbers.** Veronica is on v7, SMRITI has a documented Phase 1 → Phase 2 upgrade table. Nothing here is a one-shot.

<br/>

## Stack

<div align="center">
<img src="https://skillicons.dev/icons?i=c,cpp,python,ts,js,react,nextjs,vite,tailwind,fastapi,nodejs,express,docker,linux,git,figma&theme=dark" alt="stack"/>
</div>

<div align="center">
<sub>Systems: C/C++ for kernel and OS-level work · Python/FastAPI for AI backends · TypeScript/React for everything user-facing</sub>
</div>

<br/>

## Currently building

- Pushing **MahinaOS** through Phase 3 — shell polish and the local AI daemon
- Extending **Veronica's** omni-connector layer
- Applied to **PRAYAAS** (NCERT's national research grant) with an education-technology proposal

<br/>

## Stats

<div align="center">
<img height="165" src="https://github-readme-stats.vercel.app/api?username=HardikBhaskar2010&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&bg_color=0B1020&title_color=A78BFA&icon_color=06B6D4" alt="stats"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=HardikBhaskar2010&layout=compact&theme=tokyonight&hide_border=true&bg_color=0B1020&title_color=A78BFA" alt="top langs"/>
</div>

<div align="center">
<img src="https://streak-stats.demolab.com?user=HardikBhaskar2010&theme=tokyonight&hide_border=true&background=0B1020&ring=A78BFA&fire=06B6D4" alt="streak"/>
</div>

<div align="center">
<img src="https://raw.githubusercontent.com/HardikBhaskar2010/HardikBhaskar2010/output/github-contribution-grid-snake-dark.svg" alt="snake"/>
</div>

<br/>

## Reach out

<div align="center">

<a href="https://github.com/HardikBhaskar2010">
<img src="https://img.shields.io/badge/GitHub-HardikBhaskar2010-0B1020?style=for-the-badge&logo=github&logoColor=A78BFA"/>
</a>

</div>

<div align="center">
<sub>Building it clean. Building it bold. Building it in the open — mostly.</sub>
</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,100:0B1020&height=100&section=footer" alt="footer" width="100%"/>
