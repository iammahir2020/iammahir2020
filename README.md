<div align="center">

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg"><img src="assets/header-dark.svg" alt="Mahir Al Kamal — Software Engineer, Dhaka"></picture>

<a href="https://mahir-portfolio-five.vercel.app"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-work-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/btn-work-light.svg"><img src="assets/btn-work-dark.svg" alt="See my work" width="200"></picture></a>&nbsp;&nbsp;<a href="assets/Mahir_Al_Kamal_CV.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-cv-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/btn-cv-light.svg"><img src="assets/btn-cv-dark.svg" alt="Download my CV" width="290"></picture></a>

<a href="https://linkedin.com/in/mahiralkamal"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-linkedin-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/pill-linkedin-light.svg"><img src="assets/pill-linkedin-dark.svg" alt="LinkedIn"></picture></a>&nbsp;<a href="mailto:mahiralkamal.mak@gmail.com"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-email-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/pill-email-light.svg"><img src="assets/pill-email-dark.svg" alt="Email"></picture></a>&nbsp;<a href="https://mahir-portfolio-five.vercel.app"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/pill-portfolio-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/pill-portfolio-light.svg"><img src="assets/pill-portfolio-dark.svg" alt="Portfolio"></picture></a>

</div>

<br/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-01-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/sec-01-light.svg"><img src="assets/sec-01-dark.svg" alt="01 — About me"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/about-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/about-light.svg"><img src="assets/about-dark.svg" alt="Highlights: almost 4 years building React and Node.js apps for government and enterprise clients; worked on national platforms for the Bangladesh Election Commission and the Anti-Corruption Commission; built an AI grading tool with a model I trained, piloted in a live class; mentored two interns who were later hired full-time. Right now: looking for a full-time Software Engineer role; MSc in Computer Science at IUB, expected 2027; researching how LLMs pick ML algorithms for medical datasets; teaching the Algorithms and Data Structures labs; working spec-first with Claude Code."></picture>

<br/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-02-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/sec-02-light.svg"><img src="assets/sec-02-dark.svg" alt="02 — Experience"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/experience-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/experience-light.svg"><img src="assets/experience-dark.svg" alt="Penta Global Limited, Software Engineer, Oct 2023 to present: Neustring (B2B telecom roaming analytics for a US client, with tables, charts and exports that stay fast on large datasets, plus Amazon QuickSight dashboards); Election Management and Online Nomination System for the Bangladesh Election Commission (step-by-step nomination forms and role-based screens, every action traceable for audit); ACC ERP for the Anti-Corruption Commission (role-gated modules and long multi-step forms with drafts that save); moved legacy Jinja and jQuery screens to React without stopping feature work. Stack: React, TypeScript, Redux Toolkit, RTK Query, Amazon QuickSight. Independent University, Bangladesh, Adjunct Faculty and Research Assistant and Part-Time Frontend Developer, Dec 2022 to present: teach the Algorithms and Data Structures labs in Python with browser-based algorithm visualizers I built; research on LLM-Based Algorithm Selection for Tabular Medical Datasets (manuscript in preparation); worked on the frontend of IUB&#x27;s public website."></picture>

<br/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-03-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/sec-03-light.svg"><img src="assets/sec-03-dark.svg" alt="03 — Personal Projects"></picture>

<img src="assets/card-scanner.svg" alt="01 · Computer vision · Exam Script Mark Scanner"/>

<table>
<tr>
<td width="32%" valign="top" align="center">
<img src="assets/scanner-demo.gif" alt="Scanner walkthrough" width="230"/>
</td>
<td valign="top">

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/scanner-detail-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/scanner-detail-light.svg"><img src="assets/scanner-detail-dark.svg" alt="I was copying marks off paper exam scripts into Excel by hand every exam. Now I photograph the cover page, check every value, and the marks land in the spreadsheet. Piloted in a live university class. OpenCV finds and straightens the marks grid, then cuts it into cells; a local CNN, or Tesseract with a Gemini Vision fallback, sits behind one interface. The CNN I trained in PyTorch reads 91.8% of handwritten ID digits correctly, against 44.5% for Tesseract. Hosted on AWS with rate limiting and an origin guard; 259 pytest and 383 Vitest tests. Python, FastAPI, OpenCV, PyTorch, ONNX, Gemini API, React, TypeScript, AWS Lambda."></picture>

</td>
</tr>
</table>

<p><a href="https://d2n2meq17rr1oi.cloudfront.net"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-live-demo-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-live-demo-light.svg"><img src="assets/link-live-demo-dark.svg" alt="Live demo"></picture></a>&nbsp;<a href="https://github.com/iammahir2020/marks-upload"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-code-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-code-light.svg"><img src="assets/link-code-dark.svg" alt="Code"></picture></a></p>

<details>
<summary><code>HOW IT WORKS</code> &nbsp;architecture diagram</summary>
<br/>

```mermaid
flowchart LR
    T["📱 Teacher's phone<br/>React + TypeScript PWA"]
    Q[("IndexedDB<br/>session + upload queue")]
    X["📊 Excel export<br/>(in the browser)"]

    subgraph AWS["AWS"]
        CF["CloudFront"]
        S3[("S3<br/>static site")]
        AG["API Gateway"]
        subgraph L["Lambda container · FastAPI"]
            G["Upload checks<br/>rate limit · origin secret"]
            D["OpenCV<br/>find + straighten grid,<br/>cut cells"]
            R{{"Recognizer<br/>(one interface)"}}
            C["Local CNN<br/>ONNX · default"]
            RM["Remote<br/>Tesseract + Gemini Vision"]
        end
        CW["CloudWatch + X-Ray"]
    end

    T <--> Q
    T -->|"photo of marks grid"| CF
    CF --> S3
    CF -->|"/api + secret header"| AG --> G --> D --> R
    R --> C
    R --> RM
    R -->|"ID, serial, marks,<br/>low-confidence flags"| T
    T -->|"teacher confirms<br/>every value"| X
    L -.-> CW
```

The recognizer is picked once at startup, so the pipeline never cares which one is running. The local CNN became the default after it beat Tesseract on real class photos, and it needs no network and has no rate limit to hit mid-class.

</details>

<br/>

<img src="assets/card-polashi.svg" alt="02 · Multiplayer game · Battle of Polashi"/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/polashi-detail-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/polashi-detail-light.svg"><img src="assets/polashi-detail-dark.svg" alt="An unofficial online version of Polashi, Playground Inc.&#x27;s hidden-role board game, built so our group could play from their own phones. The server enforces every rule, so a player with devtools open can&#x27;t cheat, and each player only receives their own view, so hidden roles never leak. Every Socket.IO event validated with zod; reconnect tokens put players back in their own seat after a refresh. Audited it as an attacker and closed what I found: rate limits per socket and per IP, origin checks, message caps. Moved from Firestore to PostgreSQL with versioned migrations, without breaking play; live rooms survive a deploy. About 70 backend and 240 frontend tests, plus Playwright runs of a full 5-player game. Node.js, Express 5, Socket.IO, PostgreSQL, zod, React 19, TypeScript, Playwright."></picture>

<p align="center"><img src="assets/polashi-demo.gif" alt="A six-player game of Polashi from create room to game over" width="680"/></p>

<p><a href="https://the-great-polashi-game.vercel.app"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-play-live-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-play-live-light.svg"><img src="assets/link-play-live-dark.svg" alt="Play it live"></picture></a>&nbsp;<a href="https://github.com/iammahir2020/polashi_game_backend"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-backend-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-backend-light.svg"><img src="assets/link-backend-dark.svg" alt="Backend"></picture></a>&nbsp;<a href="https://github.com/iammahir2020/polashi_game_frontend"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-frontend-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-frontend-light.svg"><img src="assets/link-frontend-dark.svg" alt="Frontend"></picture></a></p>

<br/>

<img src="assets/card-dse.svg" alt="03 · Realtime alerts · DSE Market Monitor"/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dse-detail-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/dse-detail-light.svg"><img src="assets/dse-detail-dark.svg" alt="Watching Dhaka Stock Exchange prices meant refreshing a page and hoping to catch the move. Investors set price, percentage or volume alerts, the service checks them every two minutes, and the alert lands on a live dashboard and on Telegram. Cooldowns and de-duplication so nobody gets spammed; phone OTP login, JWT sessions, authenticated WebSockets; Telegram bot linked by one-time deep links. Node.js, Express, MongoDB, WebSockets, Telegram Bot API, React."></picture>

<p><a href="https://dse-monitor-frontend.vercel.app"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-live-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-live-light.svg"><img src="assets/link-live-dark.svg" alt="Live"></picture></a>&nbsp;<a href="https://github.com/iammahir2020/dse-monitor-backend"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-backend-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-backend-light.svg"><img src="assets/link-backend-dark.svg" alt="Backend"></picture></a>&nbsp;<a href="https://github.com/iammahir2020/dse-monitor-frontend"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-frontend-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-frontend-light.svg"><img src="assets/link-frontend-dark.svg" alt="Frontend"></picture></a></p>

<br/>

<img src="assets/card-aws.svg" alt="04 · Cloud architecture · Event-Driven BFF on AWS"/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/aws-detail-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/aws-detail-light.svg"><img src="assets/aws-detail-dark.svg" alt="I wanted AWS experience that went past tutorials, so I built the same backend-for-frontend pattern twice: GraphQL subscriptions in CDK, and REST plus WebSockets in SAM. DynamoDB Streams to AppSync, pushing every write to open browsers; EventBridge to SQS (with a dead-letter queue) to Lambda; Cognito auth, plus a custom Lambda JWT authorizer. AWS CDK, SAM, Lambda, DynamoDB, AppSync, EventBridge, SQS, Cognito."></picture>

<p><a href="https://github.com/iammahir2020/bff-practice"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-cdk-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-cdk-light.svg"><img src="assets/link-cdk-dark.svg" alt="CDK build"></picture></a>&nbsp;<a href="https://github.com/iammahir2020/aws-bff-price-alert"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-sam-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-sam-light.svg"><img src="assets/link-sam-dark.svg" alt="SAM build"></picture></a></p>

<details>
<summary><code>MORE</code> &nbsp;ZipGrip Tooling, e-commerce with Stripe payments</summary>
<br/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/zipgrip-detail-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/zipgrip-detail-light.svg"><img src="assets/zipgrip-detail-dark.svg" alt="ZipGrip Tooling: a storefront from cart to checkout, with Stripe handling the payment step so card data never touches the app&#x27;s own servers. JWT auth and role-based access on the server separate the customer and admin views. React, Node.js, Express, MongoDB, Stripe."></picture>

<p><a href="https://zipgrip-tooling.web.app/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-live-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-live-light.svg"><img src="assets/link-live-dark.svg" alt="Live"></picture></a>&nbsp;<a href="https://github.com/iammahir2020/zipGrip-tooling-client"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-client-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-client-light.svg"><img src="assets/link-client-dark.svg" alt="Client"></picture></a>&nbsp;<a href="https://github.com/iammahir2020/zipGrip-tooling-server"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/link-server-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/link-server-light.svg"><img src="assets/link-server-dark.svg" alt="Server"></picture></a></p>

</details>

<br/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-04-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/sec-04-light.svg"><img src="assets/sec-04-dark.svg" alt="04 — Stack"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/stack-light.svg"><img src="assets/stack-dark.svg" alt="Frontend: React, Next.js, TypeScript, JavaScript, Redux, Tailwind, Vite, HTML, CSS. Backend: Node.js, Express, FastAPI, Python, GraphQL. Data: PostgreSQL, MongoDB, DynamoDB, Supabase. AI: PyTorch, OpenCV, Gemini API, ONNX, RAG (research). Cloud and tools: AWS, Docker, GitHub Actions, Git, Vercel, Figma."></picture>

<br/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-05-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/sec-05-light.svg"><img src="assets/sec-05-dark.svg" alt="05 — Currently exploring"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/exploring-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/exploring-light.svg"><img src="assets/exploring-dark.svg" alt="Agentic workflows and MCP, LangChain and RAG, NestJS, Next.js caching, system design"></picture>

<br/>

<picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/iammahir2020/iammahir2020/output/activity-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/iammahir2020/iammahir2020/output/activity-light.svg"><img src="https://raw.githubusercontent.com/iammahir2020/iammahir2020/output/activity-dark.svg" alt="Contribution activity for the last 12 months"></picture>

<br/>

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sec-06-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/sec-06-light.svg"><img src="assets/sec-06-dark.svg" alt="06 — Let's build"></picture>

<div align="center">

<a href="https://mahir-portfolio-five.vercel.app"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-work-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/btn-work-light.svg"><img src="assets/btn-work-dark.svg" alt="See my work" width="200"></picture></a>&nbsp;&nbsp;<a href="assets/Mahir_Al_Kamal_CV.pdf"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/btn-cv-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/btn-cv-light.svg"><img src="assets/btn-cv-dark.svg" alt="Download my CV" width="290"></picture></a>

<sub>`MAHIRALKAMAL.MAK@GMAIL.COM` &nbsp;·&nbsp; `DHAKA, BANGLADESH`</sub>

</div>
