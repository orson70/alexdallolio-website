"""Contenuti delle pagine servizi e casi studio (IT + EN).

Solo fatti già presenti sul sito: niente prezzi, tempi o numeri inventati.
Sezioni: ("prose", h2, html) · ("films", h2, [film...]) · ("faq", h2, [(q, a)...])
Film: {"yt": id, "t": titolo, "s": sottotitolo} oppure {"src": "/file.mp4", ...}
"""

W_GERD = "ySthwmhR-y4"
W_BUILDERHERO = "UYnvGmCuroQ"
W_RAILWAYS = "mOygY_ZPATQ"
W_PROGETTO_ITALIA = "z-GjfCZasFo"
W_WESEARCH = "pbGWFFmW1Fc"
W_NIARCHOS = "nfpBWwwjCTw"
W_DREAM = "FnKHGWT7FgE"
W_GERD_TEASER = "03Y4JbKL5F0"
TETRA = "588LDT1c3zs"
CALIDA = "fAwmTQlsNTs"
FILA_FBOX = "zJ28dM8DRYo"
AI_WAKEUP = "r0N34NuRFZc"
AI_IAP = "pbjb2oghBaE"
AI_DELLALA = "B4Rv_BOayx8"
SHOWREEL = "N7Ta9EZstzA"

PAGES = {
    # ─────────────────────────────────────────────────────────────
    "archive": {
        "it": {
            "path": "/it/video-aziendali-da-archivio.html",
            "title": "Video aziendali da materiale d'archivio | Alex Dallolio, regista a Milano",
            "description": "Video aziendali e corporate costruiti dal materiale che l'azienda ha già: archivio, girato di cantiere, immagini di prodotto, render. Regia di Alex Dallolio, Milano.",
            "crumb": "Video aziendali da archivio",
            "label": "Video aziendali · Corporate · Istituzionali",
            "h1": "Il video aziendale<br>è già nel vostro <em>archivio.</em>",
            "lede": "Quasi ogni azienda ha ore di girato, foto, render e materiale tecnico che nessuno guarda più. Io parto da lì e ne tiro fuori un film: per il sito, per una fiera, per una presentazione o per un lancio interno.",
            "sections": [
                ("prose", "Da dove si parte", """
<p>La maggior parte delle produzioni comincia da una location, una troupe e un piano di riprese. Le mie spesso cominciano da quello che l'azienda possiede già:</p>
<ul>
<li><strong>Archivio video</strong>: girato di cantiere, eventi, vecchi spot, interviste.</li>
<li><strong>Immagini di prodotto</strong>: foto, cataloghi, still life.</li>
<li><strong>Materiale tecnico</strong>: render, disegni, animazioni, dati.</li>
<li><strong>Frammenti</strong>: fotografie storiche, riprese d'epoca, materiale sparso tra reparti diversi.</li>
</ul>
<p>La regia non è solo quello che succede sul set. È saper vedere struttura, ritmo, tensione e significato dentro il materiale grezzo.</p>
"""),
                ("prose", "Come lavoro", """
<p><strong>Mi mandate quello che avete.</strong> Lo guardo tutto e vi dico se dentro c'è un film, e che tipo di film.</p>
<p>Poi costruisco concept, montaggio, ritmo, musica e trattamento visivo. Dove l'archivio non basta uso l'AI generativa per estendere, riquadrare o immaginare le immagini che mancano. Quando serve davvero si gira, ma in modo mirato.</p>
<p>Lavoro da remoto. Niente trasferte, niente giornate di produzione, niente permessi. Sono a Milano, ma se il materiale esiste la geografia conta poco.</p>
"""),
                ("films", "Alcuni video aziendali", [
                    {"yt": W_GERD, "t": "GERD", "s": "Webuild · Documentario"},
                    {"yt": W_BUILDERHERO, "t": "Builderhero", "s": "Webuild · Corporate"},
                    {"yt": W_RAILWAYS, "t": "Railways Experience", "s": "Webuild · Corporate"},
                    {"yt": W_PROGETTO_ITALIA, "t": "Progetto Italia", "s": "Salini Impregilo"},
                    {"yt": TETRA, "t": "Custodiamo il domani", "s": "Tetra Pak · Corporate"},
                    {"yt": CALIDA, "t": "Calida Group", "s": "Corporate"},
                ]),
                ("faq", "Domande frequenti", [
                    ("Bisogna organizzare delle riprese?",
                     "Spesso no. Si parte dal materiale che c'è già. Se manca qualcosa si valuta insieme: immagini generate con l'AI oppure poche riprese mirate."),
                    ("Che materiale posso mandare?",
                     "Tutto quello che avete: girato d'archivio, eventi, foto, cataloghi, render, presentazioni, materiale tecnico. Anche se sembra poco o disordinato: capire cosa c'è dentro è parte del mio lavoro."),
                    ("A cosa servono questi video?",
                     "Siti web, fiere, presentazioni, campagne, lanci interni, case history. Dallo stesso materiale si possono ricavare più versioni e formati."),
                    ("Lavori solo a Milano?",
                     "No. Sono basato a Milano ma lavoro da remoto con aziende ovunque."),
                    ("Come si comincia?",
                     "Scrivetemi o prenotate una call e raccontatemi cosa avete. Vi dico se c'è un film e che forma può prendere."),
                ]),
            ],
        },
        "en": {
            "path": "/corporate-films-from-existing-footage.html",
            "title": "Corporate Films from Existing Footage and Archive | Alex Dallolio",
            "description": "Corporate and brand films built from the material a company already has: archive, site footage, product images, renders. Directed by Alex Dallolio, Milan.",
            "crumb": "Corporate films from existing footage",
            "label": "Corporate films · Brand films · Archive",
            "h1": "Your corporate film<br>is already in your <em>archive.</em>",
            "lede": "Most companies own hours of footage, photos, renders and technical material that nobody looks at anymore. I start there and find the film inside it: for your website, a trade fair, a presentation or an internal launch.",
            "sections": [
                ("prose", "Where it starts", """
<p>Most productions begin with a location, a crew and a shooting schedule. Mine often begin with what a company already has:</p>
<ul>
<li><strong>Video archive</strong>: site footage, events, old commercials, interviews.</li>
<li><strong>Product imagery</strong>: photos, catalogues, still life.</li>
<li><strong>Technical material</strong>: renders, drawings, animations, data.</li>
<li><strong>Fragments</strong>: historical photographs, vintage footage, material scattered across departments.</li>
</ul>
<p>Direction is not only what happens on set. It is the ability to see structure, rhythm, tension and meaning inside raw material.</p>
"""),
                ("prose", "How I work", """
<p><strong>You send me what you have.</strong> I go through all of it and tell you whether there is a film inside, and what kind of film.</p>
<p>Then I build concept, editing, rhythm, music and visual treatment. Where the archive falls short, I use generative AI to extend, reframe or imagine the missing images. When a shoot is truly needed, it is a targeted one.</p>
<p>I work remotely. No travel, no production days, no permits. I am based in Milan, but if the material exists, geography matters less.</p>
"""),
                ("films", "Selected corporate films", [
                    {"yt": W_GERD, "t": "GERD", "s": "Webuild · Documentary"},
                    {"yt": W_BUILDERHERO, "t": "Builderhero", "s": "Webuild · Corporate"},
                    {"yt": W_RAILWAYS, "t": "Railways Experience", "s": "Webuild · Corporate"},
                    {"yt": W_PROGETTO_ITALIA, "t": "Progetto Italia", "s": "Salini Impregilo"},
                    {"yt": TETRA, "t": "Custodiamo il domani", "s": "Tetra Pak · Corporate"},
                    {"yt": CALIDA, "t": "Calida Group", "s": "Corporate"},
                ]),
                ("faq", "Frequently asked questions", [
                    ("Do we need to organise a shoot?",
                     "Often not. We start from what already exists. If something is missing, we decide together: AI-generated imagery or a few targeted shots."),
                    ("What material can I send?",
                     "Everything you have: archive footage, events, photos, catalogues, renders, presentations, technical material. Even if it looks thin or messy: figuring out what is inside is part of my job."),
                    ("What are these films used for?",
                     "Websites, trade fairs, presentations, campaigns, internal launches, case studies. The same material can produce several versions and formats."),
                    ("Do you only work in Milan?",
                     "No. I am based in Milan and work remotely with companies anywhere."),
                    ("How do we start?",
                     "Write to me or book a call and tell me what you have. I will tell you if there is a film and what shape it can take."),
                ]),
            ],
        },
    },
    # ─────────────────────────────────────────────────────────────
    "ai": {
        "it": {
            "path": "/it/video-aziendali-ai.html",
            "title": "Video aziendali e brand film con l'AI generativa | Alex Dallolio",
            "description": "Video aziendali, brand film e fashion film realizzati con l'intelligenza artificiale generativa, diretti da un regista. Alex Dallolio, Milano: FILA, AI reel, progetti sperimentali.",
            "crumb": "Video con l'AI",
            "label": "AI generativa · Brand film · Fashion film",
            "h1": "Video con l'AI,<br>ma <em>diretti.</em>",
            "lede": "L'intelligenza artificiale genera immagini. Un film è un'altra cosa: serve qualcuno che scelga, tagli, dia ritmo e senso. Uso l'AI generativa come parte del processo di regia, non come scorciatoia.",
            "sections": [
                ("prose", "Cosa si può fare", """
<ul>
<li><strong>Film interamente generati</strong>, come il reel qui sotto: nessuna ripresa, solo regia.</li>
<li><strong>Film misti</strong>: materiale reale dell'azienda più immagini generate che lo completano, lo estendono o lo reinventano.</li>
<li><strong>Fashion e prodotto</strong>: dalle immagini di campagna e di prodotto a un film, senza allestire un set.</li>
</ul>
<p>Per la collezione FILA FW26, presentata alla Milano Fashion Week, ho fatto cinque fashion film: tre diretti sul set, due creati senza girare un solo fotogramma.</p>
"""),
                ("films", "Reel AI", [
                    {"src": "/ai-reel.mp4", "t": "AI Reel 2026", "s": "Interamente generato"},
                ]),
                ("prose", "Diretto, non solo promptato", """
<p>Chiunque oggi può scrivere un prompt. La differenza la fanno le stesse cose di sempre: concept, montaggio, ritmo, musica, trattamento visivo. Faccio immagini da trent'anni, prima con il disegno e il collage, poi con il cinema e la pubblicità. L'AI è l'ultimo strumento, non il punto di partenza.</p>
<p>Altri film AI sono su Instagram: <a href="https://www.instagram.com/alexdallolio_aifilms/" target="_blank" rel="noopener">@alexdallolio_aifilms</a>.</p>
"""),
                ("films", "Altri lavori con l'AI", [
                    {"yt": FILA_FBOX, "t": "FILA F-Box", "s": "Installazione AI · Salone del Mobile 2023"},
                    {"yt": AI_WAKEUP, "t": "Wake Up!", "s": "AI & Concept"},
                    {"yt": AI_IAP, "t": "Influencer IAP", "s": "AI & Concept"},
                    {"yt": AI_DELLALA, "t": "Atomic Dream Dance", "s": "Dell Ala · Videoclip AI"},
                ]),
                ("faq", "Domande frequenti", [
                    ("Il video è fatto tutto con l'AI?",
                     "Dipende dal progetto. Può essere interamente generato oppure misto: materiale reale dell'azienda completato da immagini generate. Si decide in base a cosa c'è e a cosa serve."),
                    ("Si possono usare le immagini dei nostri prodotti?",
                     "Sì. Le immagini di prodotto e di campagna sono uno dei punti di partenza più comuni."),
                    ("Che differenza c'è con un video fatto da un'app AI?",
                     "La regia. Un'app produce clip; un film ha una struttura, un ritmo e un'idea. È lo stesso lavoro di sempre, con strumenti nuovi."),
                    ("Come si comincia?",
                     "Raccontatemi il progetto e mandatemi il materiale che avete. Vi dico cosa si può costruire."),
                ]),
            ],
        },
        "en": {
            "path": "/ai-brand-films.html",
            "title": "AI Brand Films and Corporate Videos, Directed | Alex Dallolio",
            "description": "Corporate videos, brand films and fashion films made with generative AI and directed by a filmmaker. Alex Dallolio, Milan: FILA, AI reel, experimental work.",
            "crumb": "AI films",
            "label": "Generative AI · Brand films · Fashion films",
            "h1": "AI films,<br>but <em>directed.</em>",
            "lede": "Artificial intelligence generates images. A film is something else: someone has to choose, cut, and give it rhythm and meaning. I use generative AI as part of the directing process, not as a shortcut.",
            "sections": [
                ("prose", "What it can do", """
<ul>
<li><strong>Fully generated films</strong>, like the reel below: no shoot, only direction.</li>
<li><strong>Hybrid films</strong>: a company's real material plus generated imagery that completes, extends or reinvents it.</li>
<li><strong>Fashion and product</strong>: from campaign and product imagery to a film, without building a set.</li>
</ul>
<p>For the FILA FW26 collection, presented at Milan Fashion Week, I made five fashion films: three directed on set, two created without shooting a single frame.</p>
"""),
                ("films", "AI reel", [
                    {"src": "/ai-reel.mp4", "t": "AI Reel 2026", "s": "Fully generated"},
                ]),
                ("prose", "Directed, not just prompted", """
<p>Anyone can write a prompt today. What makes the difference is what always did: concept, editing, rhythm, music, visual treatment. I have been making images for thirty years, first drawing and collage, then cinema and advertising. AI is the latest tool, not the starting point.</p>
<p>More AI films on Instagram: <a href="https://www.instagram.com/alexdallolio_aifilms/" target="_blank" rel="noopener">@alexdallolio_aifilms</a>.</p>
"""),
                ("films", "More AI work", [
                    {"yt": FILA_FBOX, "t": "FILA F-Box", "s": "AI installation · Salone del Mobile 2023"},
                    {"yt": AI_WAKEUP, "t": "Wake Up!", "s": "AI & Concept"},
                    {"yt": AI_IAP, "t": "Influencer IAP", "s": "AI & Concept"},
                    {"yt": AI_DELLALA, "t": "Atomic Dream Dance", "s": "Dell Ala · AI music video"},
                ]),
                ("faq", "Frequently asked questions", [
                    ("Is the film made entirely with AI?",
                     "It depends on the project. It can be fully generated or hybrid: real company material completed by generated imagery. We decide based on what exists and what is needed."),
                    ("Can you use our product images?",
                     "Yes. Product and campaign imagery is one of the most common starting points."),
                    ("How is this different from a video made with an AI app?",
                     "Direction. An app produces clips; a film has structure, rhythm and an idea. It is the same craft as always, with new tools."),
                    ("How do we start?",
                     "Tell me about the project and send me the material you have. I will tell you what can be built."),
                ]),
            ],
        },
    },
    # ─────────────────────────────────────────────────────────────
    "webuild": {
        "it": {
            "path": "/it/webuild-caso-studio.html",
            "title": "Webuild: undici anni di film aziendali | Caso studio, Alex Dallolio",
            "description": "Undici anni di film per Webuild (ex Salini Impregilo): la diga GERD, WeSearch, Progetto Italia, Railways Experience. Video aziendali costruiti da girato di cantiere, archivio e materiale tecnico.",
            "crumb": "Caso studio · Webuild",
            "label": "Caso studio · Corporate · Grandi opere",
            "h1": "Webuild.<br>Undici anni di <em>grandi opere</em> in film.",
            "lede": "Da undici anni faccio film per il gruppo dietro alcuni dei più grandi progetti di costruzione del mondo: dalla diga GERD a WeSearch e Progetto Italia.",
            "sections": [
                ("prose", "Il materiale", """
<p>Un cantiere produce una quantità enorme di immagini: riprese dei lavori, droni, fotografie tecniche, render, interviste, archivio storico. Quasi mai nasce come racconto.</p>
<p>Gran parte dei film per Webuild è costruita proprio da lì: girato di cantiere, archivio e materiale tecnico, trasformati in film che le persone guardano davvero.</p>
"""),
                ("films", "Film per Webuild", [
                    {"yt": W_GERD, "t": "GERD", "s": "Grand Ethiopian Renaissance Dam"},
                    {"yt": W_GERD_TEASER, "t": "GERD Teaser", "s": "Documentario"},
                    {"yt": W_WESEARCH, "t": "WeSearch 2025", "s": "Webuild · Corporate"},
                    {"yt": W_PROGETTO_ITALIA, "t": "Progetto Italia", "s": "Salini Impregilo"},
                    {"yt": W_RAILWAYS, "t": "Railways Experience", "s": "Webuild · Corporate"},
                    {"yt": W_BUILDERHERO, "t": "Builderhero", "s": "Webuild · Corporate"},
                    {"yt": W_NIARCHOS, "t": "Stavros Niarchos", "s": "Webuild · Corporate"},
                    {"yt": W_DREAM, "t": "Dream Builders", "s": "Webuild · Corporate"},
                ]),
                ("prose", "Cosa dimostra", """
<p>Che un'azienda industriale non ha bisogno di una grande produzione per avere dei film. Ha bisogno di qualcuno che sappia vedere cosa c'è nel materiale che produce ogni giorno.</p>
<p>Se la vostra azienda ha un archivio simile, <a href="/it/video-aziendali-da-archivio.html">qui spiego come lavoro</a>.</p>
"""),
            ],
        },
        "en": {
            "path": "/webuild-case-study.html",
            "title": "Webuild: Eleven Years of Corporate Films | Case Study, Alex Dallolio",
            "description": "Eleven years of films for Webuild (formerly Salini Impregilo): the GERD dam, WeSearch, Progetto Italia, Railways Experience. Corporate films built from site footage, archive and technical material.",
            "crumb": "Case study · Webuild",
            "label": "Case study · Corporate · Infrastructure",
            "h1": "Webuild.<br>Eleven years of <em>great works</em> on film.",
            "lede": "For eleven years I have been making films for the group behind some of the world's largest construction projects: from the GERD dam to WeSearch and Progetto Italia.",
            "sections": [
                ("prose", "The material", """
<p>A construction site produces a huge amount of imagery: progress footage, drones, technical photography, renders, interviews, historical archive. It is almost never born as a story.</p>
<p>Much of the work for Webuild is built from exactly that: site footage, archive and technical material, turned into films people actually watch.</p>
"""),
                ("films", "Films for Webuild", [
                    {"yt": W_GERD, "t": "GERD", "s": "Grand Ethiopian Renaissance Dam"},
                    {"yt": W_GERD_TEASER, "t": "GERD Teaser", "s": "Documentary"},
                    {"yt": W_WESEARCH, "t": "WeSearch 2025", "s": "Webuild · Corporate"},
                    {"yt": W_PROGETTO_ITALIA, "t": "Progetto Italia", "s": "Salini Impregilo"},
                    {"yt": W_RAILWAYS, "t": "Railways Experience", "s": "Webuild · Corporate"},
                    {"yt": W_BUILDERHERO, "t": "Builderhero", "s": "Webuild · Corporate"},
                    {"yt": W_NIARCHOS, "t": "Stavros Niarchos", "s": "Webuild · Corporate"},
                    {"yt": W_DREAM, "t": "Dream Builders", "s": "Webuild · Corporate"},
                ]),
                ("prose", "What it shows", """
<p>That an industrial company does not need a large production to have films. It needs someone who can see what is inside the material it produces every day.</p>
<p>If your company has a similar archive, <a href="/corporate-films-from-existing-footage.html">here is how I work</a>.</p>
"""),
            ],
        },
    },
    # ─────────────────────────────────────────────────────────────
    "fila": {
        "it": {
            "path": "/it/fila-fashion-film.html",
            "title": "FILA FW26: fashion film sul set e con l'AI | Caso studio, Alex Dallolio",
            "description": "Cinque fashion film per la collezione FILA FW26 presentati alla Milano Fashion Week: tre diretti sul set, due creati con l'AI senza girare un fotogramma. E l'installazione AI F-Box al Salone del Mobile 2023.",
            "crumb": "Caso studio · FILA",
            "label": "Caso studio · Fashion film · AI",
            "h1": "FILA.<br>Tre film sul set, due <em>senza set.</em>",
            "lede": "Per la collezione FILA FW26, presentata alla Milano Fashion Week, ho fatto cinque fashion film: tre diretti sul set, due creati senza girare un solo fotogramma.",
            "sections": [
                ("prose", "Stessa collezione, due strade", """
<p>Il set e l'AI generativa, nello stesso progetto e con la stessa regia. I film girati e quelli generati dovevano stare insieme: stesso sguardo, stesso ritmo, stessa collezione.</p>
<p>È il modo in cui lavoro oggi: scelgo lo strumento in base a quello che serve al film, non il contrario.</p>
"""),
                ("films", "FILA FW26", [
                    {"ig": "DXgtfvYBFMP", "t": "FILA FW26", "s": "Pubblicato da FILA sul profilo ufficiale @fila_global"},
                    {"ig": "DYHmdXQOWYZ", "t": "FILA FW26 · Milano Fashion Week", "s": "Pubblicato da FILA Japan @fila_japan_official"},
                ]),
                ("films", "FILA F-Box, Salone del Mobile 2023", [
                    {"yt": FILA_FBOX, "t": "FILA F-Box", "s": "Installazione AI · Milano Design Week 2023"},
                ]),
                ("prose", "Prima ancora: F-Box", """
<p>Nel 2023, al Salone del Mobile, l'esperienza AI FILA F-Box: un'installazione per la Milano Design Week.</p>
<p>Altri esempi di <a href="/it/video-aziendali-ai.html">video e brand film con l'AI</a>.</p>
"""),
            ],
        },
        "en": {
            "path": "/fila-fashion-films.html",
            "title": "FILA FW26 Fashion Films, On Set and with AI | Case Study, Alex Dallolio",
            "description": "Five fashion films for the FILA FW26 collection presented at Milan Fashion Week: three directed on set, two created with AI without shooting a single frame. Plus the F-Box AI installation at Salone del Mobile 2023.",
            "crumb": "Case study · FILA",
            "label": "Case study · Fashion film · AI",
            "h1": "FILA.<br>Three films on set, two <em>without one.</em>",
            "lede": "For the FILA FW26 collection, presented at Milan Fashion Week, I made five fashion films: three directed on set, two created without shooting a single frame.",
            "sections": [
                ("prose", "One collection, two paths", """
<p>The set and generative AI, in the same project and under the same direction. The shot films and the generated ones had to belong together: same eye, same rhythm, same collection.</p>
<p>That is how I work today: I choose the tool based on what the film needs, not the other way around.</p>
"""),
                ("films", "FILA FW26", [
                    {"ig": "DXgtfvYBFMP", "t": "FILA FW26", "s": "Published by FILA on its official account @fila_global"},
                    {"ig": "DYHmdXQOWYZ", "t": "FILA FW26 · Milan Fashion Week", "s": "Published by FILA Japan @fila_japan_official"},
                ]),
                ("films", "FILA F-Box, Salone del Mobile 2023", [
                    {"yt": FILA_FBOX, "t": "FILA F-Box", "s": "AI installation · Milan Design Week 2023"},
                ]),
                ("prose", "Before that: F-Box", """
<p>In 2023, at Salone del Mobile, the FILA F-Box AI experience: an installation for Milan Design Week.</p>
<p>More <a href="/ai-brand-films.html">AI brand films and videos</a>.</p>
"""),
            ],
        },
    },
    # ─────────────────────────────────────────────────────────────
    # Reel da @alexdallolio_aifilms, aggiornati da ~/CLAUDE/SITO_ALEXDALLOLIO/sync_aifilms.py
    "aifilms": {
        "it": {
            "path": "/it/ai-films.html",
            "title": "Taccuino: appunti AI, brevi film fatti con l'AI | Alex Dallolio",
            "description": "I brevi film di Alex Dallolio realizzati con l'intelligenza artificiale generativa: luoghi, persone e atmosfere che non esistono. Un reel nuovo ogni pochi giorni.",
            "crumb": "Taccuino",
            "label": "Appunti AI · da Instagram",
            "h1": "Taccuino.<br><em>Appunti AI.</em>",
            "lede": "Idee provate con l'AI appena pensate, una dopo l'altra. Clicca un appunto per vederlo con l'audio.",
            "sections": [
                ("reels", "Tutti gli appunti"),
                ("prose", "Seguili su Instagram", """
<p>Ogni film esce prima su <a href="https://www.instagram.com/alexdallolio_aifilms/" target="_blank" rel="noopener">@alexdallolio_aifilms</a>. Se ti interessa come l'AI può entrare nei film della tua azienda, <a href="/it/video-aziendali-ai.html">qui spiego come lavoro</a>.</p>
"""),
            ],
        },
        "en": {
            "path": "/ai-films.html",
            "title": "Notebook: AI Sketches, Short Films Made with AI | Alex Dallolio",
            "description": "Short films by Alex Dallolio made with generative AI: places, people and moods that do not exist. A new reel every few days.",
            "crumb": "Notebook",
            "label": "AI sketches · from Instagram",
            "h1": "Notebook.<br><em>AI sketches.</em>",
            "lede": "Ideas tried with AI as soon as they come, one after another. Click a sketch to watch it with sound.",
            "sections": [
                ("reels", "All sketches"),
                ("prose", "Follow on Instagram", """
<p>Every film comes out first on <a href="https://www.instagram.com/alexdallolio_aifilms/" target="_blank" rel="noopener">@alexdallolio_aifilms</a>. If you are curious how AI can work in your company's films, <a href="/ai-brand-films.html">here is how I work</a>.</p>
"""),
            ],
        },
    },
}

# Testi fissi dell'interfaccia
UI = {
    "it": {
        "nav_work": "Lavori", "nav_all": "Tutti i film", "nav_contact": "Contatti",
        "related": "Continua", "footer_city": "Milano",
        "cta_h2": "Mandatemi quello che avete.<br><em>Vi dico se dentro c'è un film.</em>",
        "cta_p": "Archivio, immagini di prodotto, una case history, un evento o solo un problema da risolvere.",
        "cta_email": "Scrivimi", "cta_book": "Prenota una call",
    },
    "en": {
        "nav_work": "Work", "nav_all": "All films", "nav_contact": "Contact",
        "related": "Keep exploring", "footer_city": "Milan",
        "cta_h2": "Send me what you have.<br><em>I will tell you if there is a film inside.</em>",
        "cta_p": "Archive footage, product images, a case study, an event, or just a problem to solve.",
        "cta_email": "Email me", "cta_book": "Book a call",
    },
}

# Etichette brevi per i link incrociati tra pagine
SHORT = {
    "archive": {"it": ("Servizio", "Video aziendali da archivio"), "en": ("Service", "Corporate films from existing footage")},
    "ai": {"it": ("Servizio", "Video e brand film con l'AI"), "en": ("Service", "AI brand films")},
    "webuild": {"it": ("Caso studio", "Webuild, undici anni di film"), "en": ("Case study", "Webuild, eleven years of films")},
    "fila": {"it": ("Caso studio", "FILA FW26, set e AI"), "en": ("Case study", "FILA FW26, set and AI")},
    "aifilms": {"it": ("Taccuino", "Appunti AI"), "en": ("Notebook", "AI sketches")},
}
