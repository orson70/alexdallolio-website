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

# Selezione privata: i testi restano qui, in una lista semplice da aggiornare.
# "A modo mio" (16/11/2026): sei film raccontati nella voce di Alex, dal dubbio alla soluzione.
# Fatti dettati da Alex il 16/11 (F-Box, Transpack, Leonardo, WeSearch). FW26 ed Egoiste: solo fatti gia noti, niente dettagli dedotti.
A_MODO_MIO_CASES = [
    {"titolo": 'FILA F-Box', "sotto": 'FILA · Salone del Mobile 2023', "yt": FILA_FBOX,
     "testo": "Cinquant'anni di FILA, la Design Week, e il logo, l'F-Box. Era il 2023, un mondo in cui l'intelligenza artificiale non riusciva ancora a fare le scritte, le chiedevi una F e ti tornava un'altra cosa... e il lavoro era tutto su un logo. L'intuizione è stata quella: se riesco a costruire la possibilità di quella scritta, con un'AI proprio agli inizi, poi posso raccontare delle storie. Una tecnica di time lapse, e ogni volta una storia diversa, ma partendo sempre dal logo."},
    {"titolo": 'FILA FW26', "sotto": 'FILA · Milano Fashion Week', "yt": "", "ig": ["DXgtfvYBFMP", "DYHmdXQOWYZ"],
     "testo": "Cinque film per la collezione, Milano Fashion Week. Tre li ho girati sul set, come si è sempre fatto. Gli altri due li ho fatti senza girare un fotogramma, e lì il dubbio era uno solo: messi vicino agli altri, si vedrà la cucitura? Credo che il trucco sia non cambiare sguardo solo perché cambia l'attrezzo. FILA li ha pubblicati sui suoi profili. I due senza set sono questi qui sopra, ma così non vale, te l'ho detto io."},
    {"titolo": 'Fake / Egoïste', "sotto": 'Ricerca personale · 2026', "yt": "", "ig": "DfINAfLBD6e",
     "testo": "Qui il cliente non c'era, me lo sono chiesto da solo. Un omaggio a Égoïste di Jean-Paul Goude, che era una produzione enorme, un luogo costruito apposta, decine di interpreti, un coro... Si può rifare lo spirito di una cosa così senza set e senza troupe? Non lo so ancora, forse no. Però è venuto fuori, costruito un'inquadratura alla volta, e il lavoro alla fine era quello di sempre: scegliere, tagliare, dare il ritmo."},
    {"titolo": 'Custodiamo il domani', "sotto": 'Transpack Group · Corporate', "yt": "588LDT1c3zs",
     "testo": "Un gruppo che da più di cinquant'anni fa imballaggi di carta e legno, e un film che doveva essere istituzionale, molto istituzionale. Qui volevo essere preciso: casse enormi riprese come col braccio, il porto, proprio le loro cose. L'ho fatto un anno fa, quando l'intelligenza artificiale non era quella di adesso, e ho dovuto un po' impazzire: il reale dove c'era, il resto generato, mischiati. Niente uffici, niente impiegati al computer... ho cercato di far parlare un'azienda che vende ad altre aziende come un marchio, con una specie di filosofia unica, un linguaggio suo."},
    {"titolo": 'Leonardo', "sotto": 'Webuild · 2024', "yt": "f52oa8DJdXo",
     "testo": "Una mostra su Leonardo in Australia, e Webuild che vuole legare il Leonardo ingegnere alle opere che costruisce oggi. Tutto è partito da una lettera, quella in cui si offre a Ludovico il Moro, che in un certo senso è il primo curriculum della storia: elenca tutto quello che sa fare, ponti, canali, edifici... che poi sono le stesse cose che fa Webuild. Non ricordo più se l'idea sia stata nostra o del cliente. Il guaio era che il protagonista è morto da cinquecento anni e di lui restano disegni e codici, mica riprese. Però c'era l'AI di prima generazione, ancora grezza, e per una cosa era il sistema migliore: prendere i disegni di Leonardo e trasformarli nelle opere di Webuild. Un filo rosso tra il mondo antico e quello moderno... e gli italiani di questa conoscenza sono i depositari, credo."},
    {"titolo": 'WeSearch 2025', "sotto": 'Webuild · Film di fine anno', "yt": "pbGWFFmW1Fc",
     "testo": 'Il film di fine anno del gruppo: premi, cantieri, contratti nuovi, numeri, un anno intero in due minuti. Al cliente quelle cose servono precise, sono coordinate, numeri, spesso economici, e gliele devi dare esatte. La frase era la loro, «Nel 2024 abbiamo cercato…». Ma un elenco di numeri resta una slide... allora ho provato a fondere due cose: una grafica che gli dà esattamente i suoi punti, e un viaggio, con dentro elementi che portano avanti il racconto senza appesantirlo. O almeno ci ho provato.'},
]
A_MODO_MIO_CASES_EN = [
    {"titolo": 'FILA F-Box', "sotto": 'FILA · Salone del Mobile 2023', "yt": FILA_FBOX,
     "testo": "Fifty years of FILA, Design Week, and the logo, the F-Box. It was 2023, a world where artificial intelligence still couldn't do lettering, you asked for an F and got something else back... and the whole job was about a logo. That was the intuition: if I can build the possibility of that lettering, with an AI at its very beginnings, then I can tell stories. A time-lapse technique, a different story each time, but always starting from the logo."},
    {"titolo": 'FILA FW26', "sotto": 'FILA · Milan Fashion Week', "yt": "", "ig": ["DXgtfvYBFMP", "DYHmdXQOWYZ"],
     "testo": "Five films for the collection, Milan Fashion Week. Three I shot on set, the way it has always been done. The other two I made without shooting a single frame, and there was only one doubt: next to the others, will the seam show? I think the trick is not to change your eye just because the tool changes. FILA published them on its own profiles. The two without a set are the ones above, but that's cheating, I just told you."},
    {"titolo": 'Fake / Egoïste', "sotto": 'Personal research · 2026', "yt": "", "ig": "DfINAfLBD6e",
     "testo": "No client here, I asked it of myself. A homage to Égoïste by Jean-Paul Goude, which was a huge production, a location built for it, dozens of performers, a chorus... Can you redo the spirit of something like that with no set and no crew? I still don't know, maybe not. But it came out, built one shot at a time, and in the end the work was the usual one: choosing, cutting, giving it rhythm."},
    {"titolo": 'Custodiamo il domani', "sotto": 'Transpack Group · Corporate', "yt": "588LDT1c3zs",
     "testo": "A group that has been making paper and wood packaging for more than fifty years, and a film that had to be institutional, very institutional. Here I wanted to be precise: huge crates filmed as if from a crane, the port, their own things. I made it a year ago, when artificial intelligence wasn't what it is now, and it drove me a little crazy: the real where it existed, the rest generated, mixed together. No offices, no people at their computers... I tried to make a company that sells to other companies speak like a brand, with a kind of philosophy of its own, a language of its own."},
    {"titolo": 'Leonardo', "sotto": 'Webuild · 2024', "yt": "f52oa8DJdXo",
     "testo": "An exhibition on Leonardo in Australia, and Webuild wanting to tie Leonardo the engineer to the works it builds today. It all started from a letter, the one in which he offers himself to Ludovico il Moro, which in a way is the first CV in history: it lists everything he can do, bridges, canals, buildings... which happen to be the same things Webuild does. I no longer remember whether the idea was ours or the client's. The trouble was that the lead has been dead for five hundred years and what's left of him is drawings and codices, not footage. But there was first-generation AI, still rough, and for one thing it was the best system: taking Leonardo's drawings and turning them into Webuild's works. A red thread between the ancient world and the modern one... and Italians are the keepers of that knowledge, I think."},
    {"titolo": 'WeSearch 2025', "sotto": 'Webuild · End-of-year film', "yt": "pbGWFFmW1Fc",
     "testo": "The group's end-of-year film: awards, sites, new contracts, numbers, a whole year in two minutes. The client needs those things exact, they are coordinates, figures, often financial, and you have to give them exactly. The line was theirs, «In 2024 we searched for…». But a list of figures is still a slide... so I tried to fuse two things: graphics that give them exactly their points, and a journey, with elements inside that carry the story forward without weighing it down. Or at least I tried."},
]

SELEZIONE_AI_CASES = [
    {"titolo": "FILA F-Box", "sotto": "FILA · Salone del Mobile 2023", "yt": FILA_FBOX,
     "brief": "Per i cinquant'anni del marchio, alla Milano Design Week: prendere l'F-Box, il logo storico di FILA, e farlo esplorare, scomporre e reinventare dall'intelligenza artificiale.",
     "problema": "Nel 2023 l'AI generativa non sapeva scrivere. Lettere e loghi uscivano deformati: ogni F diventava un'altra cosa. E il lavoro era tutto su una lettera.",
     "soluzione": "Ho smesso di chiederle di scrivere. Ho trovato il modo di farle riconoscere la F come forma, non come testo. Da lì il logo ha potuto esplodere nello spazio, moltiplicarsi e tornare a sé stesso.",
     "agenzia": "Un marchio storico reinventato per un evento, senza toccare il logo e senza tradirlo."},
    {"titolo": "FILA FW26", "sotto": "FILA · Milano Fashion Week", "yt": "", "ig": ["DXgtfvYBFMP", "DYHmdXQOWYZ"],
     "brief": "Cinque fashion film per la collezione FW26, presentata alla Milano Fashion Week e pubblicata da FILA sui suoi profili ufficiali.",
     "problema": "Tre film si potevano girare sul set. Due chiedevano luoghi che non esistono. E dovevano stare accanto agli altri tre senza che si vedesse la cucitura: stessa collezione, stessi capi, stesso sguardo.",
     "soluzione": "Tre diretti sul set, due creati senza girare un fotogramma: sono i due qui sopra. Stessa regia, stessa luce, stesso montaggio: FILA li ha pubblicati insieme, come un'unica campagna.",
     "agenzia": "Una campagna in cui il set e l'AI lavorano insieme, e il cliente vede solo la collezione."},
    {"titolo": "Fake / Egoïste", "sotto": "Ricerca personale · 2026", "yt": "", "ig": "DfINAfLBD6e",
     "brief": "Nessun cliente: un brief che mi sono dato. Un omaggio a Égoïste, il film di Jean-Paul Goude, partendo da una stanza vera, dalle sue finestre e dalle donne che ci ho visto dentro.",
     "problema": "Quel film era una produzione enorme: un luogo costruito, decine di interpreti, un coro. Rifarne lo spirito senza girare vuol dire tenere coerenti luogo, volti e ritmo da un'inquadratura all'altra.",
     "soluzione": "Un minuto di film senza set e senza troupe, costruito inquadratura per inquadratura. La regia fa quello che fa sempre: sceglie, taglia, dà ritmo.",
     "agenzia": "L'idea ambiziosa che di solito muore al preventivo, portata al cliente già fatta."},
    {"titolo": "Custodiamo il domani", "sotto": "Transpack Group · Corporate", "yt": TETRA,
     "brief": "Il film istituzionale di un gruppo che da oltre cinquant'anni fa imballaggi in carta e legno. Con una promessa da far vedere: proteggere i beni, le persone, il pianeta.",
     "problema": "Un imballaggio è fatto per sparire: lo apri e lo butti. E natura, cura, materia che si trasforma sono parole che in uno stabilimento non si lasciano filmare.",
     "soluzione": "Ho tenuto vero il lavoro e ho generato quello che la fabbrica non poteva mostrare: la natura da cui parte la materia, la carta e il legno che cambiano forma sotto gli occhi.",
     "agenzia": "Un film di valori per un'azienda industriale che non ha immagini all'altezza delle sue parole."},
    {"titolo": "Leonardo", "sotto": "Webuild · 2024", "yt": "f52oa8DJdXo",
     "brief": "Per la mostra «Leonardo da Vinci – 500 Years of Genius» in Australia, Webuild voleva un film che legasse il Leonardo ingegnere alle opere che il gruppo costruisce oggi.",
     "problema": "Il protagonista è morto da cinquecento anni. Di lui restano disegni e codici, non immagini da montare.",
     "soluzione": "Ho fatto parlare lui. La voce legge la lettera con cui Leonardo si offre a Ludovico il Moro come ingegnere: ponti, canali, edifici. Le immagini generate gli danno un corpo, una bottega, una Firenze.",
     "agenzia": "Un anniversario, un fondatore, una storia d'archivio: il passato del cliente che torna in scena."},
    {"titolo": "WeSearch 2025", "sotto": "Webuild · Film di fine anno", "yt": W_WESEARCH,
     "brief": "Il film di fine anno del gruppo: premi, cantieri, nuovi contratti, numeri. Un 2024 intero in due minuti.",
     "problema": "Un elenco di risultati è una slide, non un film. E le opere sono sparse per il mondo, con immagini di ogni qualità e provenienza.",
     "soluzione": "Un'idea sola: una barra di ricerca. «Nel 2024 abbiamo cercato…» e ogni risultato dell'anno diventa una risposta. Le scene generate fanno da ponte tra un cantiere e l'altro e danno a tutto la stessa mano.",
     "agenzia": "Il bilancio dell'anno, la convention, il report: i numeri del cliente in un film che si guarda fino in fondo."},
]

SELEZIONE_AI_CASES_EN = [
    {"titolo": "FILA F-Box", "sotto": "FILA · Salone del Mobile 2023", "yt": FILA_FBOX,
     "brief": "For the brand's fiftieth anniversary, at Milan Design Week: take the F-Box, FILA's historic logo, and let artificial intelligence explore it, take it apart and reinvent it.",
     "problema": "In 2023 generative AI could not write. Letters and logos came out deformed: every F turned into something else. And the whole job was about one letter.",
     "soluzione": "I stopped asking it to write. I found a way to make it recognise the F as a shape, not as text. From there the logo could explode in space, multiply and come back to itself.",
     "agenzia": "A heritage brand reinvented for an event, without touching the logo and without betraying it."},
    {"titolo": "FILA FW26", "sotto": "FILA · Milan Fashion Week", "yt": "", "ig": ["DXgtfvYBFMP", "DYHmdXQOWYZ"],
     "brief": "Five fashion films for the FW26 collection, presented at Milan Fashion Week and published by FILA on its official accounts.",
     "problema": "Three films could be shot on set. Two called for places that do not exist. And they had to sit next to the other three with no visible seam: same collection, same garments, same eye.",
     "soluzione": "Three directed on set, two created without shooting a single frame: the two above. Same direction, same light, same editing: FILA published them together, as one campaign.",
     "agenzia": "A campaign where the set and AI work together, and the client only sees the collection."},
    {"titolo": "Fake / Egoïste", "sotto": "Personal work · 2026", "yt": "", "ig": "DfINAfLBD6e",
     "brief": "No client: a brief I gave myself. An homage to Égoïste, the film by Jean-Paul Goude, starting from a real room, its windows and the women I saw in it.",
     "problema": "That film was a huge production: a built location, dozens of performers, a chorus. Recreating its spirit without shooting means keeping place, faces and rhythm consistent from one shot to the next.",
     "soluzione": "One minute of film with no set and no crew, built shot by shot. Direction does what it always does: it chooses, cuts, gives rhythm.",
     "agenzia": "The ambitious idea that usually dies at the quote, brought to the client already made."},
    {"titolo": "Custodiamo il domani", "sotto": "Transpack Group · Corporate", "yt": TETRA,
     "brief": "The corporate film of a group that has been making paper and wood packaging for over fifty years. With a promise to make visible: protecting goods, people, the planet.",
     "problema": "Packaging is made to disappear: you open it and throw it away. And nature, care, matter that transforms are words that do not let themselves be filmed in a factory.",
     "soluzione": "I kept the work real and generated what the factory could not show: the nature the material comes from, paper and wood changing shape before your eyes.",
     "agenzia": "A film about values for an industrial company whose images do not live up to its words."},
    {"titolo": "Leonardo", "sotto": "Webuild · 2024", "yt": "f52oa8DJdXo",
     "brief": "For the exhibition “Leonardo da Vinci – 500 Years of Genius” in Australia, Webuild wanted a film linking Leonardo the engineer to the works the group builds today.",
     "problema": "The lead character has been dead for five hundred years. What remains of him are drawings and codices, not footage to edit.",
     "soluzione": "I let him speak. The voice reads the letter in which Leonardo offers himself to Ludovico il Moro as an engineer: bridges, canals, buildings. The generated images give him a body, a workshop, a Florence.",
     "agenzia": "An anniversary, a founder, an archive story: the client's past back on stage."},
    {"titolo": "WeSearch 2025", "sotto": "Webuild · Year-end film", "yt": W_WESEARCH,
     "brief": "The group's year-end film: awards, sites, new contracts, numbers. A whole 2024 in two minutes.",
     "problema": "A list of results is a slide, not a film. And the works are scattered around the world, with images of every quality and origin.",
     "soluzione": "One idea: a search bar. “Throughout 2024 we searched for…” and every result of the year becomes an answer. The generated scenes bridge one site and the next and give everything the same hand.",
     "agenzia": "The annual results, the convention, the report: the client's numbers in a film people watch to the end."},
]

PAGES = {
    "a_modo_mio": {
        "it": {
            "path": "/it/a-modo-mio.html",
            "title": "A modo mio: sei film fatti con l'AI | Alex Dallolio, regista a Milano",
            "description": "Sei film fatti con l'intelligenza artificiale, raccontati da chi li ha diretti: il dubbio da cui è partito ognuno e come è stato risolto. FILA, Webuild, Transpack.",
            "crumb": "A modo mio",
            "label": "Sei film · il dubbio, poi il film",
            "h1": "A modo <em>mio.</em>",
            "lede": "Un cliente di solito vuole che il suo marchio si veda, grande, e ha pure ragione, lo paga lui... io però finisco sempre a cercare un'altra cosa, quella che non si vede. Prima, per film così, c'era l'image bank: immagini di altri, buone per tutti, e ti toccava restare sul vago, sull'emozione. Oggi posso essere preciso, proprio le tue cose, e posso togliere quello che non serve più, gli uffici, gli impiegati al computer. L'intelligenza artificiale ormai la usa chiunque. E allora cosa cambia? Forse solo il modo di guardare, credo.",
            "sections": [("cases", "", A_MODO_MIO_CASES)],
        },
        "en": {
            "path": "/my-way.html",
            "title": "My way: six films made with AI | Alex Dallolio, film director in Milan",
            "description": "Six films made with artificial intelligence, told by the director who made them: the doubt each one started from and how it was solved. FILA, Webuild, Transpack.",
            "crumb": "My way",
            "label": "Six films · the doubt, then the film",
            "h1": "My <em>way.</em>",
            "lede": "A client usually wants the brand to be seen, big, and fair enough, they're paying... but I always end up looking for something else, the thing you don't see. For films like these there used to be the image bank: other people's pictures, good for everyone, so you had to stay vague, emotional. Today I can be precise, your own things, and I can take out what's no longer needed, the offices, the people at their computers. Everyone uses artificial intelligence by now. So what changes? Maybe only the way of looking, I think.",
            "sections": [("cases", "", A_MODO_MIO_CASES_EN)],
        },
    },
    "selezione_ai": {
        "it": {
            "path": "/it/selezione-ai.html",
            "title": "Sei film fatti con l'AI | Alex Dallolio",
            "description": "Sei casi di film fatti con l'intelligenza artificiale.",
            "crumb": "Selezione AI",
            "label": "Selezione privata · AI",
            "h1": "Sei film che non si potevano <em>girare.</em>",
            "lede": "Sei brief che chiedevano un set, una troupe o un budget che non c'era. Per ognuno: la richiesta, l'ostacolo, la soluzione. E quello che può proporre al suo cliente un'agenzia con un regista così alle spalle.",
            "single_language": True,
            "lang_switch": True,
            "noindex": True,
            "sections": [("cases", "", SELEZIONE_AI_CASES)],
        },
        "en": {
            "path": "/selezione-ai.html",
            "title": "Six films made with AI | Alex Dallolio",
            "description": "Six case studies of films made with artificial intelligence.",
            "crumb": "AI selection",
            "label": "Private selection · AI",
            "h1": "Six films that could not be <em>shot.</em>",
            "lede": "Six briefs that called for a set, a crew or a budget that was not there. For each one: the request, the obstacle, the solution. And what an agency can pitch to its client with a director like this behind it.",
            "single_language": True,
            "lang_switch": True,
            "noindex": True,
            "sections": [("cases", "", SELEZIONE_AI_CASES_EN)],
        },
    },
    # ─────────────────────────────────────────────────────────────
    "archive": {
        "it": {
            "path": "/it/video-aziendali-da-archivio.html",
            "title": "Video aziendali da materiale d'archivio | Alex Dallolio, regista a Milano",
            "description": "Video aziendali e corporate costruiti dal materiale che l'azienda ha già: archivio, girato di cantiere, immagini di prodotto, render. Regia di Alex Dallolio, Milano.",
            "crumb": "Brand film da archivio",
            "label": "Brand film · Corporate · Istituzionali",
            "h1": "Il film<br>è già nel tuo <em>archivio.</em>",
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
<p><strong>Mandami quello che hai.</strong> Lo guardo tutto e ti dico se dentro c'è un film, e che tipo di film.</p>
<p>Poi costruisco concept, montaggio, ritmo, musica e trattamento visivo. Dove l'archivio non basta uso l'AI generativa per estendere, riquadrare o immaginare le immagini che mancano. Quando serve davvero si gira, ma in modo mirato.</p>
<p>Gran parte del lavoro si fa a distanza: tu mi mandi il materiale, io lo trasformo. Sono a Milano, ma se il materiale esiste la geografia conta poco.</p>
"""),
                ("films", "Alcuni brand film", [
                    {"yt": W_GERD, "t": "GERD", "s": "Webuild · Documentario"},
                    {"yt": W_BUILDERHERO, "t": "Builderhero", "s": "Webuild · Corporate"},
                    {"yt": W_RAILWAYS, "t": "Railways Experience", "s": "Webuild · Corporate"},
                    {"yt": W_PROGETTO_ITALIA, "t": "Progetto Italia", "s": "Salini Impregilo"},
                    {"yt": TETRA, "t": "Custodiamo il domani", "s": "Transpack · Corporate"},
                    {"yt": CALIDA, "t": "Calida Group", "s": "Corporate"},
                ]),
                ("faq", "Domande frequenti", [
                    ("Bisogna organizzare delle riprese?",
                     "Spesso no. Si parte dal materiale che c'è già. Se manca qualcosa si valuta insieme: immagini generate con l'AI oppure poche riprese mirate."),
                    ("Che materiale posso mandare?",
                     "Tutto quello che hai: girato d'archivio, eventi, foto, cataloghi, render, presentazioni, materiale tecnico. Anche se sembra poco o disordinato: capire cosa c'è dentro è parte del mio lavoro."),
                    ("A cosa servono questi video?",
                     "Siti web, fiere, presentazioni, campagne, lanci interni, case history. Dallo stesso materiale si possono ricavare più versioni e formati."),
                    ("Lavori solo a Milano?",
                     "No. Vivo e lavoro a Milano, e lavoro a distanza con aziende di tutto il mondo."),
                    ("Come si comincia?",
                     "Scrivimi o prenota una call e raccontami cosa hai. Partiamo da lì."),
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
<li><strong>Product imagery</strong>: photos, catalogs, still life.</li>
<li><strong>Technical material</strong>: renders, drawings, animations, data.</li>
<li><strong>Fragments</strong>: historical photographs, vintage footage, material scattered across departments.</li>
</ul>
<p>Direction is not only what happens on set. It is the ability to see structure, rhythm, tension and meaning inside raw material.</p>
"""),
                ("prose", "How I work", """
<p><strong>You send me what you have.</strong> I go through all of it and tell you whether there is a film inside, and what kind of film.</p>
<p>Then I build concept, editing, rhythm, music and visual treatment. Where the archive falls short, I use generative AI to extend, reframe or imagine the missing images. When a shoot is truly needed, it is a targeted one.</p>
<p>Much of the work happens remotely: you send the material, I shape it. I am based in Milan, but if the material exists, geography matters less.</p>
"""),
                ("films", "Selected corporate films", [
                    {"yt": W_GERD, "t": "GERD", "s": "Webuild · Documentary"},
                    {"yt": W_BUILDERHERO, "t": "Builderhero", "s": "Webuild · Corporate"},
                    {"yt": W_RAILWAYS, "t": "Railways Experience", "s": "Webuild · Corporate"},
                    {"yt": W_PROGETTO_ITALIA, "t": "Progetto Italia", "s": "Salini Impregilo"},
                    {"yt": TETRA, "t": "Custodiamo il domani", "s": "Transpack · Corporate"},
                    {"yt": CALIDA, "t": "Calida Group", "s": "Corporate"},
                ]),
                ("faq", "Frequently asked questions", [
                    ("Do we need to organize a shoot?",
                     "Often not. We start from what already exists. If something is missing, we decide together: AI-generated imagery or a few targeted shots."),
                    ("What material can I send?",
                     "Everything you have: archive footage, events, photos, catalogs, renders, presentations, technical material. Even if it looks thin or messy: figuring out what is inside is part of my job."),
                    ("What are these films used for?",
                     "Websites, trade fairs, presentations, campaigns, internal launches, case studies. The same material can produce several versions and formats."),
                    ("Do you only work in Milan?",
                     "No. I am based in Milan and work remotely with companies anywhere."),
                    ("How do we start?",
                     "Write to me or book a call and tell me what you have. We start from there."),
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
            "lede": "L'intelligenza artificiale genera immagini. Un film è un'altra cosa: serve qualcuno che scelga, tagli, dia ritmo e senso. Uso l'AI generativa dentro la regia, come uno strumento tra gli altri.",
            "sections": [
                ("prose", "Cosa si può fare", """
<ul>
<li><strong>Film interamente generati</strong>, come il reel qui sotto: nessuna ripresa, solo regia.</li>
<li><strong>Film misti</strong>: materiale reale dell'azienda più immagini generate che lo completano, lo estendono o lo reinventano.</li>
<li><strong>Fashion e prodotto</strong>: dalle immagini di campagna e di prodotto a un film, senza allestire un set.</li>
</ul>
<p>Per FILA FW26 ho usato le due strade insieme: tre film girati sul set, due generati. <a href="/it/fila-fashion-film.html">Il caso FILA →</a></p>
"""),
                ("films", "Reel AI", [
                    {"src": "/ai-reel.mp4", "t": "AI Reel 2026", "s": "Interamente generato"},
                ]),
                ("prose", "Diretto, non solo promptato", """
<p>Chiunque oggi può scrivere un prompt. La differenza la fanno le stesse cose di sempre: concept, montaggio, ritmo, musica, trattamento visivo. Faccio immagini da sempre, prima con il disegno e il collage, poi con il cinema e la pubblicità. L'AI è l'ultimo strumento che ho preso in mano.</p>
<p>Gli appunti AI sono nel <a href="/it/ai-films.html">Taccuino</a> e su Instagram: <a href="https://www.instagram.com/alexdallolio_aifilms/" target="_blank" rel="noopener">@alexdallolio_aifilms</a>.</p>
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
                     "Raccontami il progetto e mandami il materiale che hai. Ti dico cosa si può costruire."),
                ]),
            ],
        },
        "en": {
            "path": "/ai-brand-films.html",
            "title": "AI Brand Films and Corporate Videos, Directed | Alex Dallolio",
            "description": "Corporate videos, brand films and fashion films made with generative AI and directed by a filmmaker. Alex Dallolio, Milan: FILA, AI reel, experimental work.",
            "crumb": "AI brand films",
            "label": "Generative AI · Brand films · Fashion films",
            "h1": "AI films,<br>but <em>directed.</em>",
            "lede": "Artificial intelligence generates images. A film is something else: someone has to choose, cut, and give it rhythm and meaning. I use generative AI inside the directing, as one tool among others.",
            "sections": [
                ("prose", "What it can do", """
<ul>
<li><strong>Fully generated films</strong>, like the reel below: no shoot, only direction.</li>
<li><strong>Hybrid films</strong>: a company's real material plus generated imagery that completes, extends or reinvents it.</li>
<li><strong>Fashion and product</strong>: from campaign and product imagery to a film, without building a set.</li>
</ul>
<p>For FILA FW26 I used both paths together: three films shot on set, two generated. <a href="/fila-fashion-films.html">The FILA case →</a></p>
"""),
                ("films", "AI reel", [
                    {"src": "/ai-reel.mp4", "t": "AI Reel 2026", "s": "Fully generated"},
                ]),
                ("prose", "Directed, not just prompted", """
<p>Anyone can write a prompt today. What makes the difference is what always did: concept, editing, rhythm, music, visual treatment. I have always made images, first drawing and collage, then cinema and advertising. AI is the latest tool I have picked up.</p>
<p>More in the <a href="/ai-films.html">Notebook</a> and on Instagram: <a href="https://www.instagram.com/alexdallolio_aifilms/" target="_blank" rel="noopener">@alexdallolio_aifilms</a>.</p>
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
            "title": "Webuild: film aziendali sulle grandi opere | Caso studio, Alex Dallolio",
            "description": "I film per Webuild (ex Salini Impregilo): diga GERD, WeSearch, Progetto Italia. Film costruiti da girato di cantiere, archivio e materiale tecnico.",
            "crumb": "Caso studio · Webuild",
            "label": "Caso studio · Corporate · Grandi opere",
            "h1": "Webuild.<br>Le <em>grandi opere</em> in film.",
            "lede": "Faccio film per il gruppo dietro alcuni dei più grandi progetti di costruzione del mondo, come la diga GERD. Dai cantieri a WeSearch e Progetto Italia.",
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
<p>Che il racconto di un'azienda spesso esiste già, nel materiale che produce ogni giorno. Serve qualcuno che sappia vederlo, e girare solo quello che manca.</p>
<p>Se la tua azienda ha un archivio simile, <a href="/it/video-aziendali-da-archivio.html">qui spiego come lavoro</a>.</p>
"""),
            ],
        },
        "en": {
            "path": "/webuild-case-study.html",
            "title": "Webuild: Corporate Films on Landmark Infrastructure | Case Study, Alex Dallolio",
            "description": "Films for Webuild (formerly Salini Impregilo): the GERD dam, WeSearch, Progetto Italia. Films built from site footage, archive and technical material.",
            "crumb": "Case study · Webuild",
            "label": "Case study · Corporate · Infrastructure",
            "h1": "Webuild.<br><em>Landmark infrastructure</em> on film.",
            "lede": "I make films for the group behind some of the world's largest construction projects, such as the GERD dam. From the sites to WeSearch and Progetto Italia.",
            "sections": [
                ("prose", "The material", """
<p>A construction site produces a huge amount of imagery: progress footage, drones, technical photography, renders, interviews, historical archive. It is almost never shot as a story.</p>
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
<p>That a company's story often already exists, in the material it produces every day. It takes someone who can see it, and shoot only what is missing.</p>
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
            "description": "Cinque fashion film per FILA FW26 alla Milano Fashion Week: tre girati sul set, due creati con l'AI. E l'installazione AI F-Box al Salone del Mobile 2023.",
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
                ("prose", "Prima ancora: F-Box", """
<p>Nel 2023, al Salone del Mobile, l'esperienza AI FILA F-Box: un'installazione per la Milano Design Week.</p>
"""),
                ("films", "", [
                    {"yt": FILA_FBOX, "t": "FILA F-Box", "s": "Installazione AI · Salone del Mobile 2023"},
                ]),
                ("prose", "", """
<p>Altri esempi di <a href="/it/video-aziendali-ai.html">video e brand film con l'AI</a>.</p>
"""),
            ],
        },
        "en": {
            "path": "/fila-fashion-films.html",
            "title": "FILA FW26 Fashion Films, on Set and with AI | Alex Dallolio",
            "description": "Five fashion films for FILA FW26 at Milan Fashion Week: three shot on set, two created with AI. Plus the F-Box AI installation at Salone del Mobile 2023.",
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
                ("prose", "Before that: F-Box", """
<p>In 2023, at Salone del Mobile, the FILA F-Box AI experience: an installation for Milan Design Week.</p>
"""),
                ("films", "", [
                    {"yt": FILA_FBOX, "t": "FILA F-Box", "s": "AI installation · Salone del Mobile 2023"},
                ]),
                ("prose", "", """
<p>More <a href="/ai-brand-films.html">AI brand films and videos</a>.</p>
"""),
            ],
        },
    },
    # ─────────────────────────────────────────────────────────────
    "fashion": {
        "it": {
            "path": "/it/fashion-film.html",
            "title": "Fashion film a Milano: regia per moda e lusso | Alex Dallolio",
            "description": "Fashion film e campagne per Prada, Canali, Chopard, Luisa Spagnoli, FILA. Regia a Milano, sul set o con l'AI generativa.",
            "crumb": "Fashion film",
            "label": "Fashion film · Moda · Lusso",
            "h1": "Fashion film.<br>La collezione, <em>in movimento.</em>",
            "lede": "Giro fashion film e campagne per la moda e il lusso: Prada, Canali, Chopard, Luisa Spagnoli, Cromia, John Richmond. Per FILA FW26 ho messo il set e l'AI generativa nella stessa collezione.",
            "sections": [
                ("prose", "Come lavoro", """
<p>Un fashion film non è un catalogo che si muove. Parte da un'idea sulla collezione: un gesto, una luce, un ritmo. Casting, set, montaggio e musica servono a quell'idea.</p>
<p>Giro sul set quando il capo va visto addosso, toccato, fatto muovere. Uso l'AI generativa quando serve un luogo che non esiste o un'immagine che nessuna produzione potrebbe permettersi. Spesso le due strade stanno nello stesso progetto.</p>
"""),
                ("films", "Fashion film e campagne", [
                    {"yt": "YVLem2cHfoc", "t": "Hands", "s": "Canali · Director's cut"},
                    {"yt": "Z3IW1Piynhc", "t": "Canali Mood", "s": "Canali · Fashion film"},
                    {"yt": "xv2S2flaYJQ", "t": "Chopard", "s": "Fashion spot"},
                    {"yt": "fA3pBdKnWbo", "t": "Prada Canali", "s": "Fashion film"},
                    {"yt": "nQpwJ2VzS6w", "t": "Luisa Spagnoli", "s": "Campagna Primavera Estate · Director's cut"},
                    {"yt": "1C1ICMJcdVk", "t": "Cromia", "s": "Campagna Autunno Inverno"},
                    {"yt": "RhJl57UGFbg", "t": "John Richmond", "s": "Spot profumo"},
                    {"yt": "sRMixFeTOKM", "t": "Perfetti Manichini", "s": "Bonaveri"},
                ]),
                ("films", "FILA FW26 · Milano Fashion Week", [
                    {"ig": "DXgtfvYBFMP", "t": "FILA FW26", "s": "Pubblicato da FILA sul profilo ufficiale @fila_global"},
                    {"ig": "DYHmdXQOWYZ", "t": "FILA FW26 · Milano Fashion Week", "s": "Pubblicato da FILA Japan @fila_japan_official"},
                ]),
                ("prose", "Dal set all'AI", """
<p>Per FILA FW26 ho fatto cinque fashion film: tre girati sul set, due generati con l'AI, con lo stesso sguardo. <a href="/it/fila-fashion-film.html">Il caso FILA →</a></p>
<p>Gli esperimenti più liberi, moda compresa, sono nel <a href="/it/ai-films.html">Taccuino</a>.</p>
"""),
                ("faq", "Domande frequenti", [
                    ("Giri anche sul set?",
                     "Sì. Molti dei miei fashion film sono girati sul set, con troupe, casting e luci. L'AI entra quando serve qualcosa che il set non può dare."),
                    ("Lavori con le agenzie o direttamente con i brand?",
                     "Con entrambi. Ho lavorato con agenzie come DLV, Young &amp; Rubicam, JWT, Leo Burnett e Armando Testa, e direttamente con i brand."),
                    ("Posso avere anche le versioni per i social?",
                     "Sì. Dallo stesso materiale si ricavano il film principale e le versioni brevi e verticali."),
                    ("Come si comincia?",
                     "Raccontami la collezione e mandami moodboard, lookbook o immagini di campagna. Partiamo da lì."),
                ]),
            ],
        },
        "en": {
            "path": "/fashion-films.html",
            "title": "Fashion Films in Milan, Fashion and Luxury | Alex Dallolio",
            "description": "Fashion films and campaigns for Prada, Canali, Chopard, Luisa Spagnoli, FILA. Directed in Milan, on set or with generative AI.",
            "crumb": "Fashion films",
            "label": "Fashion films · Fashion · Luxury",
            "h1": "Fashion films.<br>The collection, <em>in motion.</em>",
            "lede": "I direct fashion films and campaigns for fashion and luxury: Prada, Canali, Chopard, Luisa Spagnoli, Cromia, John Richmond. For FILA FW26 I brought the set and generative AI into the same collection.",
            "sections": [
                ("prose", "How I work", """
<p>A fashion film is not a catalog that moves. It starts from an idea about the collection: a gesture, a light, a rhythm. Casting, set, editing and music all serve that idea.</p>
<p>I shoot on set when a garment has to be seen on a body, touched, set in motion. I use generative AI when the film needs a place that does not exist, or an image no production could afford. Often both paths live in the same project.</p>
"""),
                ("films", "Fashion films and campaigns", [
                    {"yt": "YVLem2cHfoc", "t": "Hands", "s": "Canali · Director's cut"},
                    {"yt": "Z3IW1Piynhc", "t": "Canali Mood", "s": "Canali · Fashion film"},
                    {"yt": "xv2S2flaYJQ", "t": "Chopard", "s": "Fashion spot"},
                    {"yt": "fA3pBdKnWbo", "t": "Prada Canali", "s": "Fashion film"},
                    {"yt": "nQpwJ2VzS6w", "t": "Luisa Spagnoli", "s": "Spring Summer campaign · Director's cut"},
                    {"yt": "1C1ICMJcdVk", "t": "Cromia", "s": "Fall Winter campaign"},
                    {"yt": "RhJl57UGFbg", "t": "John Richmond", "s": "Perfume commercial"},
                    {"yt": "sRMixFeTOKM", "t": "Perfetti Manichini", "s": "Bonaveri"},
                ]),
                ("films", "FILA FW26 · Milan Fashion Week", [
                    {"ig": "DXgtfvYBFMP", "t": "FILA FW26", "s": "Published by FILA on its official account @fila_global"},
                    {"ig": "DYHmdXQOWYZ", "t": "FILA FW26 · Milan Fashion Week", "s": "Published by FILA Japan @fila_japan_official"},
                ]),
                ("prose", "From set to AI", """
<p>For FILA FW26 I made five fashion films: three shot on set, two generated with AI, with the same eye. <a href="/fila-fashion-films.html">The FILA case →</a></p>
<p>The freer experiments, fashion included, are in the <a href="/ai-films.html">Notebook</a>.</p>
"""),
                ("faq", "Frequently asked questions", [
                    ("Do you also shoot on set?",
                     "Yes. Many of my fashion films are shot on set, with a crew, casting and lighting. AI comes in when the film needs something a set cannot give."),
                    ("Do you work with agencies or directly with brands?",
                     "Both. I have worked with agencies such as DLV, Young &amp; Rubicam, JWT, Leo Burnett and Armando Testa, and directly with brands."),
                    ("Can I also get versions for social media?",
                     "Yes. The same material gives the main film plus short and vertical cuts."),
                    ("How do we start?",
                     "Tell me about the collection and send me a moodboard, lookbook or campaign images. We start from there."),
                ]),
            ],
        },
    },
    # ─────────────────────────────────────────────────────────────
    # Reel da @alexdallolio_aifilms, aggiornati da ~/CLAUDE/SITO_ALEXDALLOLIO/sync_aifilms.py
    "aifilms": {
        "it": {
            "path": "/it/ai-films.html",
            "title": "Taccuino. Appunti AI, brevi film | Alex Dallolio",
            "description": "I brevi film di Alex Dallolio realizzati con l'intelligenza artificiale generativa: luoghi, persone e atmosfere che non esistono. Un reel nuovo ogni pochi giorni.",
            "crumb": "Taccuino",
            "label": "Appunti AI · da Instagram",
            "h1": "Taccuino.<br><em>Appunti AI.</em>",
            "lede": "Idee provate con l'AI appena pensate, una dopo l'altra. Clicca un appunto per vederlo con l'audio.",
            "sections": [
                ("reels", "Tutti gli appunti"),
                ("prose", "Seguili su Instagram", """
<p>Ogni film esce prima su <a href="https://www.instagram.com/alexdallolio_aifilms/" target="_blank" rel="noopener">@alexdallolio_aifilms</a>. Se ti interessa come l'AI può entrare nei film della tua azienda, <a href="/it/video-aziendali-ai.html">qui spiego come lavoro</a>.</p>
<p><a href="/stanza/">Entra nella stanza →</a> Scrivi un pensiero a mano, ti risponde un film del taccuino.</p>
"""),
            ],
        },
        "en": {
            "path": "/ai-films.html",
            "title": "Notebook. AI Sketches, Short Films | Alex Dallolio",
            "description": "Short films by Alex Dallolio made with generative AI: places, people and moods that do not exist. A new reel every few days.",
            "crumb": "Notebook",
            "label": "AI sketches · from Instagram",
            "h1": "Notebook.<br><em>AI sketches.</em>",
            "lede": "Ideas tried with AI as soon as they come, one after another. Click a sketch to watch it with sound.",
            "sections": [
                ("reels", "All sketches"),
                ("prose", "Follow on Instagram", """
<p>Every film comes out first on <a href="https://www.instagram.com/alexdallolio_aifilms/" target="_blank" rel="noopener">@alexdallolio_aifilms</a>. If you are curious how AI can work in your company's films, <a href="/ai-brand-films.html">here is how I work</a>.</p>
<p><a href="/room/">Enter the room →</a> Write a thought by hand and a film from the notebook answers.</p>
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
        "cta_h2": "Mandami quello che hai.<br><em>Ti dico se dentro c'è un film.</em>",
        "cta_p": "Archivio, immagini di prodotto, una case history, un evento o solo un problema da risolvere.",
        "cta_email": "Scrivimi", "cta_book": "Prenota una call",
    },
    "en": {
        "nav_work": "Work", "nav_all": "All films", "nav_contact": "Contact",
        "related": "Keep exploring", "footer_city": "Milan",
        "cta_h2": "Send me what you have.<br><em>I'll tell you if there's a film in it.</em>",
        "cta_p": "Archive footage, product images, a case study, an event, or just a problem to solve.",
        "cta_email": "Email me", "cta_book": "Book a call",
    },
}

# Etichette brevi per i link incrociati tra pagine
SHORT = {
    "a_modo_mio": {"it": ("Sei film", "A modo mio"), "en": ("Six films", "My way")},
    "archive": {"it": ("Servizio", "Brand film da archivio"), "en": ("Service", "Corporate films from existing footage")},
    "ai": {"it": ("Servizio", "Video e brand film con l'AI"), "en": ("Service", "AI brand films")},
    "webuild": {"it": ("Caso studio", "Webuild, le grandi opere in film"), "en": ("Case study", "Webuild, landmark infrastructure on film")},
    "fila": {"it": ("Caso studio", "FILA FW26, set e AI"), "en": ("Case study", "FILA FW26, set and AI")},
    "fashion": {"it": ("Servizio", "Fashion film"), "en": ("Service", "Fashion films")},
    "aifilms": {"it": ("Taccuino", "Taccuino. Appunti AI"), "en": ("Notebook", "Notebook. AI sketches")},
}
