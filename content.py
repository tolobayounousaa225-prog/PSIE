"""Textes du site, en français et en arabe.

Sources : Statuts de la PSIE (art. 1 à 8, 10 à 18, 28 à 34, 36, 39) et Règlement Intérieur (art. 31 à 34).
Les traductions arabes sont une première version à faire relire avant la mise en ligne.
"""

SITE_NAME = {"fr": "Plateforme des Structures Islamiques d'Éducation", "ar": "منصة الهياكل الإسلامية للتعليم"}

# Pages publiées : (fichier, clé de menu, dans le plan du site ?)
PAGES = [
    ("index", "nav_home", True),
    ("apropos", "nav_about", True),
    ("gouvernance", "nav_gov", True),
    ("membres", "nav_members", True),
    ("adhesion", "nav_join", True),
    ("verification", "nav_verify", True),
    ("actualites", "nav_news", True),
    ("faq", "nav_faq", True),
    ("documents", "nav_docs", True),
    ("regions", "nav_regions", True),
    ("galerie", "nav_gallery", True),
    ("contact", "nav_contact", True),
    ("mentions", "nav_legal", True),
    ("actualite", "nav_news", False),  # détail d'une actualité : contenu chargé par JavaScript
]

T = {
    "fr": {
        # ---- commun ----
        "nav_home": "Accueil", "nav_about": "À propos", "nav_gov": "Gouvernance", "nav_members": "Nos membres",
        "nav_join": "Adhérer", "nav_verify": "Vérifier un document", "nav_news": "Actualités", "nav_faq": "FAQ",
        "nav_contact": "Contact", "nav_legal": "Mentions légales", "nav_login": "Connexion", "menu": "Menu",
        "skip": "Aller au contenu", "lang_other": "العربية", "to_top": "Haut de page",
        "footer": "© PSIE — Plateforme des Structures Islamiques d'Éducation",
        "footer_tag": "Coordonner, représenter, élever la qualité de l'éducation islamique en Côte d'Ivoire.",
        "footer_links": "Liens utiles", "footer_contact": "Nous joindre",
        "join_cta": "Demander l'adhésion", "track": "Suivre ma demande", "soon": "Bientôt disponible",
        "loading": "Chargement…", "read_more": "Lire la suite", "back": "Retour aux actualités",
        "see_all": "Toutes les actualités", "discover": "Découvrir la PSIE", "learn_more": "En savoir plus",
        "unavailable": "Ces informations sont momentanément indisponibles. Merci de réessayer plus tard.",
        "members_note": "La liste à jour est momentanément indisponible : voici les membres fondateurs.",
        "no_js": "Cette section nécessite JavaScript.", "news_none": "Aucune actualité pour le moment.",
        "cat": {"fondateur": "Membre fondateur", "ordinaire": "Membre ordinaire", "honneur": "Membre d'honneur"},
        "address": "Mosquée AL FATH, Avenue 8, Rue 15, Treichville, Abidjan",
        "address_label": "Siège", "phone_label": "Téléphone", "map": "Voir sur la carte",
        "phone1": "+225 07 07 83 63 73", "phone2": "+225 07 07 80 54 54",
        "desc_default": "Fédération qui coordonne et représente les organisations islamiques d'éducation de Côte d'Ivoire.",

        # ---- accueil ----
        "hero_kicker": "Fédération nationale",
        "hero_title_a": "Ensemble pour une éducation islamique",
        "hero_title_hl": "structurée, moderne et citoyenne",
        "hero_intro": ("La PSIE coordonne et représente les organisations nationales islamiques d'éducation auprès de "
                       "l'État de Côte d'Ivoire et des partenaires techniques et financiers de l'éducation."),
        "stats": [
            {"value": 6, "label": "organisations fondatrices"},
            {"value": 13, "label": "administrateurs au Conseil d'Administration"},
            {"value": 2, "label": "commissions techniques permanentes"},
            {"value": 41, "label": "représentations régionales (DRENA)"},
        ],
        "missions_title": "Nos missions",
        "missions_sub": "Cinq engagements au service des élèves, des enseignants et des structures islamiques d'éducation.",
        "missions": [
            {"t": "Interlocuteur crédible", "d": "Être l'interface des organisations islamiques d'éducation auprès de l'État et des partenaires techniques et financiers."},
            {"t": "Intégration et capacités", "d": "Conduire avec l'État les processus d'intégration et de renforcement de capacité des structures islamiques d'éducation."},
            {"t": "Qualité de l'éducation", "d": "Promouvoir la qualité de l'éducation islamique par le respect de normes et le renforcement des ressources humaines."},
            {"t": "Cohésion et paix", "d": "Être un acteur social de cohésion, de paix et de développement."},
            {"t": "Défense des membres", "d": "Défendre les intérêts de ses membres dans les limites fixées par les lois et les statuts."},
        ],
        "principles_title": "Nos principes",
        "principles": [
            "Respect des valeurs islamiques et républicaines", "Égalité", "Transparence",
            "Bonne gouvernance", "Redevabilité", "Collégialité",
        ],
        "steps_title": "Rejoindre la PSIE en quatre étapes",
        "steps": [
            {"t": "Déposer la demande", "d": "Remplissez le formulaire en ligne et conservez votre code de suivi."},
            {"t": "Examen par la DEN", "d": "La Direction Exécutive Nationale étudie votre dossier."},
            {"t": "Avis du Conseil d'Administration", "d": "Le CA donne son avis écrit sur l'admission."},
            {"t": "Décision de l'Assemblée Générale", "d": "L'Assemblée Générale se prononce sur l'adhésion."},
        ],
        "news_home_title": "Dernières actualités",
        "founders_title": "Les organisations fondatrices",
        "cta_title": "Votre structure éduque des enfants ?",
        "cta_text": "Rejoignez la fédération qui porte la voix de l'éducation islamique en Côte d'Ivoire.",

        # ---- à propos ----
        "desc_apropos": "Histoire, objet, missions et principes de la Plateforme des Structures Islamiques d'Éducation.",
        "about_title": "À propos de la PSIE",
        "about_lead": "Une fédération née de la volonté des organisations islamiques d'éducation de parler d'une seule voix.",
        "story_title": "Notre histoire",
        "story": [
            "Le 3 septembre 2021, les organisations et associations islamiques d'éducation de Côte d'Ivoire se sont réunies en Assemblée Générale Constitutive. Elles ont décidé de créer une structure associative à vocation fédérative pour l'orientation et la coordination des organisations islamiques d'éducation.",
            "Les statuts ont été révisés en 2026 pour renforcer la gouvernance : Conseil d'Administration, Direction Exécutive Nationale, Commissariat aux Comptes et commissions techniques permanentes.",
        ],
        "object_title": "Notre objet",
        "object": ("Coordonner et représenter les organisations nationales islamiques d'éducation dans leurs relations avec l'État de Côte d'Ivoire "
                   "et les partenaires techniques et financiers de l'éducation, en vue de la promotion d'un enseignement islamique "
                   "structuré, moderne et conforme aux valeurs républicaines."),
        "context_title": "Un cadre légal et un engagement",
        "context": [
            "La PSIE est une organisation de la société civile à but non lucratif, apolitique et non sectaire, régie par l'Ordonnance n° 2024-368 du 12 juin 2024.",
            "Elle s'inscrit dans la politique de scolarisation obligatoire (loi n° 2015-635 du 17 septembre 2015) et dans l'objectif d'intégrer les structures islamiques d'éducation au système éducatif formel.",
            "Elle considère l'éducation comme un droit fondamental de chaque enfant et agit dans son intérêt supérieur.",
        ],

        # ---- gouvernance ----
        "desc_gouvernance": "Les organes de la PSIE : Assemblée Générale, Conseil d'Administration, Direction Exécutive Nationale, Commissariat aux Comptes, commissions et représentations régionales.",
        "gov_title": "Gouvernance",
        "gov_lead": "Quatre organes, deux commissions techniques et un réseau régional : une organisation collégiale, contrôlée et transparente.",
        "chart_ag": "Assemblée Générale", "chart_ag_sub": "Organe suprême",
        "chart_ca": "Conseil d'Administration", "chart_ca_sub": "13 administrateurs",
        "chart_cc": "Commissariat aux Comptes", "chart_cc_sub": "2 commissaires",
        "chart_den": "Direction Exécutive Nationale", "chart_den_sub": "Organe d'exécution",
        "chart_com": "Commissions techniques", "chart_com_sub": "CNECI · CNVSP",
        "chart_reg": "Représentations régionales", "chart_reg_sub": "41 DRENA",
        "organs": [
            {"name": "Assemblée Générale", "tag": "Organe suprême", "points": [
                "Composée du Conseil d'Administration, du Commissariat aux Comptes, de la Direction Exécutive Nationale et des organisations membres.",
                "Annuelle (activités, rapports, budget), Ordinaire tous les trois ans (orientations, élection des organes) ou Extraordinaire (statuts, dissolution).",
                "Convoquée au moins quinze jours à l'avance ; délibère valablement à la présence des deux tiers de ses membres.",
            ]},
            {"name": "Conseil d'Administration", "tag": "Contrôle et supervision", "points": [
                "Treize administrateurs issus des six organisations fondatrices (deux par structure) ; mandat de trois ans.",
                "Veille à l'application des décisions de l'Assemblée Générale et supervise la gestion de la Direction Exécutive.",
                "Donne un avis écrit sur l'admission ou la suspension d'un membre et sur l'ordre du jour des assemblées.",
            ]},
            {"name": "Direction Exécutive Nationale", "tag": "Organe d'exécution", "points": [
                "Dirigée par le Directeur Exécutif National, avec six secrétariats, chacun assisté d'un adjoint.",
                "Administration et affaires juridiques ; formation, pédagogie et suivi des programmes ; examens, concours et vie extra-scolaire.",
                "Affaires financières et mobilisation des ressources ; information, communication et relations publiques ; intégration des écoles et ressources humaines.",
            ]},
            {"name": "Commissariat aux Comptes", "tag": "Contrôle financier", "points": [
                "Deux commissaires élus par l'Assemblée Générale pour trois ans.",
                "Accès à toutes les écritures, pièces comptables et à l'état de caisse, à toute réquisition.",
                "Rapport écrit après chaque investigation ; peut convoquer une Assemblée Générale Extraordinaire en cas de gestion de fait.",
            ]},
        ],
        "commissions_title": "Commissions techniques permanentes",
        "commissions": [
            {"sigle": "CNECI", "name": "Commission Nationale des Examens et Concours Islamiques", "points": [
                "Vérifie et valide les épreuves des examens islamiques à grand tirage.",
                "Compile les statistiques et propose les calendriers des examens.",
                "Met à disposition les documents consensuels : diplôme, relevés de notes, attestations.",
            ]},
            {"sigle": "CNVSP", "name": "Commission Nationale de Validation des Manuels et du Suivi des Programmes", "points": [
                "Veille à l'application du programme et de l'emploi du temps harmonisés.",
                "Contrôle, valide et publie la liste des manuels scolaires homologués.",
                "Exige que tout auteur ou éditeur collabore avec une organisation membre.",
            ]},
        ],
        "regional_title": "Un réseau dans toutes les régions",
        "regional": ("La PSIE est représentée dans chaque Direction Régionale de l'Éducation Nationale par un délégué régional, "
                     "actuellement dans 41 DRENA. Des délégués de circonscription assurent l'interface locale dans l'enseignement préscolaire et primaire."),
        "transparency_title": "Transparence et conformité",
        "transparency": [
            "Exercice budgétaire du 1er janvier au 31 décembre ; états financiers mis à disposition au moins quinze jours avant l'Assemblée Générale.",
            "Double signature obligatoire pour les retraits de fonds, par deux responsables issus d'organisations différentes.",
            "Registre des dons indiquant l'identité du donateur, la date, la nature et le montant ; engagement contre le blanchiment de capitaux.",
            "Déclaration des conflits d'intérêts par les membres des organes ; fonctions exercées à titre bénévole.",
        ],

        # ---- membres ----
        "desc_membres": "Les organisations membres de la PSIE et les conditions d'adhésion.",
        "members_title": "Nos membres",
        "members_lead": "Des organisations islamiques d'éducation réunies pour porter ensemble la voix de leurs structures.",
        "categories_title": "Les catégories de membres",
        "categories": [
            {"t": "Membres fondateurs", "d": "Les organisations à l'origine de la création de la PSIE, représentées à l'Assemblée Générale Constitutive."},
            {"t": "Membres ordinaires", "d": "Les organisations en charge de structures islamiques d'éducation, légalement constituées, qui adhèrent aux statuts."},
            {"t": "Membres d'honneur", "d": "Les personnes ou institutions reconnues comme telles par l'Assemblée Générale."},
        ],
        "founders": ["OEECI", "LECIM", "IQRA", "CHERIFLA", "AL HIKMA", "HINNEH"],

        # ---- adhésion ----
        "desc_adhesion": "Conditions et étapes pour adhérer à la PSIE.",
        "join_title": "Adhérer à la PSIE",
        "join_lead": "Vous êtes une organisation en charge de structures islamiques d'éducation ? Rejoignez la fédération.",
        "conditions_title": "Qui peut adhérer ?",
        "conditions_intro": "Peuvent adhérer les organisations islamiques d'éducation légalement constituées qui :",
        "conditions": [
            "approuvent les statuts de la PSIE ;",
            "s'acquittent du droit d'adhésion ;",
            "s'engagent à payer régulièrement leurs cotisations ;",
            "satisfont aux exigences et formalités d'adhésion.",
        ],
        "process_title": "Le parcours de votre demande",
        "process_note": "Le montant du droit d'adhésion et des cotisations est fixé par les organes de la PSIE. Renseignez-vous auprès du secrétariat.",
        "join_online": "Déposer ma demande en ligne",
        "join_track_text": "Vous avez déjà déposé une demande ? Suivez son avancement avec votre code.",

        # ---- vérification ----
        "desc_verification": "Vérifier l'authenticité d'un reçu, d'une attestation ou d'un certificat délivré par la PSIE.",
        "verify_title": "Vérifier un document",
        "verify_lead": "Les reçus, attestations de cotisation et certificats d'adhésion de la PSIE portent un QR code qui permet d'en contrôler l'authenticité.",
        "verify_steps": [
            "Scannez le QR code imprimé sur le document avec l'appareil photo de votre téléphone.",
            "La page de vérification s'ouvre sur le site sécurisé de la PSIE.",
            "Contrôlez que le numéro, l'organisation et le montant correspondent au document que vous détenez.",
        ],
        "verify_note": "Un reçu annulé ou une attestation qui n'est plus à jour est signalé comme tel sur la page de vérification.",

        # ---- FAQ ----
        "desc_faq": "Questions fréquentes sur la PSIE, l'adhésion et la vérification des documents.",
        "faq_title": "Questions fréquentes",
        "faq": [
            {"q": "Qu'est-ce que la PSIE ?", "a": "Une fédération qui coordonne et représente les organisations nationales islamiques d'éducation de Côte d'Ivoire auprès de l'État et des partenaires de l'éducation."},
            {"q": "Qui peut adhérer ?", "a": "Toute organisation islamique d'éducation légalement constituée qui approuve les statuts, s'acquitte du droit d'adhésion et s'engage à cotiser régulièrement."},
            {"q": "Comment adhérer ?", "a": "En déposant une demande en ligne. Elle est examinée par la Direction Exécutive Nationale, soumise à l'avis écrit du Conseil d'Administration, puis décidée par l'Assemblée Générale."},
            {"q": "Combien coûte l'adhésion ?", "a": "Le droit d'adhésion et les cotisations sont fixés par les organes de la PSIE. Contactez le secrétariat pour connaître les montants en vigueur."},
            {"q": "Comment suivre ma demande ?", "a": "Avec le code de suivi remis au dépôt de la demande, sur la page « Suivre ma demande »."},
            {"q": "Comment vérifier un reçu ou un certificat ?", "a": "En scannant son QR code : la page de vérification confirme l'authenticité du document."},
            {"q": "Qui dirige la PSIE ?", "a": "Un Directeur Exécutif National et six secrétariats assurent l'exécution ; un Conseil d'Administration de treize membres les supervise ; deux commissaires aux comptes contrôlent les finances."},
            {"q": "Où se trouve le siège ?", "a": "À Abidjan, commune de Treichville, au sein de la mosquée AL FATH, Avenue 8, Rue 15."},
        ],

        # ---- contact ----
        "desc_contact": "Coordonnées du siège de la PSIE à Abidjan.",
        "contact_title": "Nous contacter",
        "contact_lead": "Pour toute information sur la PSIE ou sur l'adhésion, joignez le secrétariat.",
        "contact_note": "Vous pouvez aussi déposer une demande d'adhésion directement en ligne.",

        # ---- mentions légales ----
        "desc_mentions": "Mentions légales et confidentialité du site de la PSIE.",
        "legal_title": "Mentions légales et confidentialité",
        "legal": [
            {"t": "Éditeur du site", "p": [
                "Plateforme des Structures Islamiques d'Éducation (PSIE), organisation de la société civile à but non lucratif régie par l'Ordonnance n° 2024-368 du 12 juin 2024.",
                "Siège : mosquée AL FATH, Avenue 8, Rue 15, Treichville, Abidjan. Directeur de la publication : le Directeur Exécutif National."]},
            {"t": "Hébergement", "p": ["Le site est hébergé par GitHub Pages. L'application d'adhésion et d'administration est hébergée sur un serveur distinct."]},
            {"t": "Cookies et mesure d'audience", "p": ["Ce site ne dépose aucun cookie et n'utilise aucun outil de mesure d'audience ni de publicité."]},
            {"t": "Données personnelles", "p": [
                "Ce site ne collecte aucune donnée personnelle. Les informations saisies dans une demande d'adhésion le sont sur l'application de la PSIE et servent uniquement à instruire cette demande.",
                "Les listes de membres et d'actualités affichées proviennent de l'application et ne contiennent que des informations publiques."]},
            {"t": "Contenu", "p": ["Les textes présentent les statuts de la PSIE. En cas de divergence, les statuts font foi."]},
        ],
    },

    "ar": {
        # ---- commun ----
        "nav_home": "الرئيسية", "nav_about": "من نحن", "nav_gov": "الحوكمة", "nav_members": "أعضاؤنا",
        "nav_join": "الانخراط", "nav_verify": "التحقق من وثيقة", "nav_news": "الأخبار", "nav_faq": "أسئلة شائعة",
        "nav_contact": "اتصل بنا", "nav_legal": "إشعارات قانونية", "nav_login": "الدخول", "menu": "القائمة",
        "skip": "انتقل إلى المحتوى", "lang_other": "Français", "to_top": "أعلى الصفحة",
        "footer": "© المنصة — منصة الهياكل الإسلامية للتعليم",
        "footer_tag": "التنسيق والتمثيل والارتقاء بجودة التعليم الإسلامي في كوت ديفوار.",
        "footer_links": "روابط مفيدة", "footer_contact": "للتواصل معنا",
        "join_cta": "طلب الانخراط", "track": "متابعة طلبي", "soon": "قريبا",
        "loading": "جار التحميل…", "read_more": "اقرأ المزيد", "back": "العودة إلى الأخبار",
        "see_all": "كل الأخبار", "discover": "اكتشف المنصة", "learn_more": "اعرف المزيد",
        "unavailable": "هذه المعلومات غير متاحة مؤقتا. يرجى إعادة المحاولة لاحقا.",
        "members_note": "القائمة المحدثة غير متاحة مؤقتا: هؤلاء هم الأعضاء المؤسسون.",
        "no_js": "يتطلب هذا القسم تفعيل جافاسكريبت.", "news_none": "لا توجد أخبار حاليا.",
        "cat": {"fondateur": "عضو مؤسس", "ordinaire": "عضو عادي", "honneur": "عضو شرف"},
        "address": "مسجد الفتح، الشارع 8، الزقاق 15، تريشفيل، أبيدجان",
        "address_label": "المقر", "phone_label": "الهاتف", "map": "عرض على الخريطة",
        "phone1": "+225 07 07 83 63 73", "phone2": "+225 07 07 80 54 54",
        "desc_default": "اتحاد ينسق ويمثل المنظمات الإسلامية للتعليم في كوت ديفوار.",

        # ---- accueil ----
        "hero_kicker": "اتحاد وطني",
        "hero_title_a": "معا من أجل تعليم إسلامي",
        "hero_title_hl": "منظم وعصري ومواطن",
        "hero_intro": ("تنسق المنصة وتمثل المنظمات الوطنية للتعليم الإسلامي لدى دولة كوت ديفوار "
                       "والشركاء التقنيين والماليين في مجال التعليم."),
        "stats": [
            {"value": 6, "label": "منظمات مؤسسة"},
            {"value": 13, "label": "عضوا في مجلس الإدارة"},
            {"value": 2, "label": "لجنتان تقنيتان دائمتان"},
            {"value": 41, "label": "تمثيلية جهوية (مديريات التعليم)"},
        ],
        "missions_title": "مهامنا",
        "missions_sub": "خمسة التزامات في خدمة التلاميذ والمعلمين والهياكل الإسلامية للتعليم.",
        "missions": [
            {"t": "محاور موثوق", "d": "أن تكون الواجهة للمنظمات الإسلامية للتعليم لدى الدولة والشركاء التقنيين والماليين."},
            {"t": "الإدماج وبناء القدرات", "d": "قيادة مسارات الإدماج وبناء القدرات للهياكل الإسلامية للتعليم بالتعاون مع الدولة."},
            {"t": "جودة التعليم", "d": "ترقية جودة التعليم الإسلامي باحترام المعايير وتعزيز الموارد البشرية."},
            {"t": "التماسك والسلم", "d": "أن تكون فاعلا اجتماعيا للتماسك والسلم والتنمية."},
            {"t": "الدفاع عن الأعضاء", "d": "الدفاع عن مصالح أعضائها في حدود ما تقرره القوانين والنظام الأساسي."},
        ],
        "principles_title": "مبادئنا",
        "principles": [
            "احترام القيم الإسلامية والجمهورية", "المساواة", "الشفافية",
            "الحوكمة الرشيدة", "المساءلة", "العمل الجماعي",
        ],
        "steps_title": "الانضمام إلى المنصة في أربع خطوات",
        "steps": [
            {"t": "تقديم الطلب", "d": "املأوا الاستمارة عبر الإنترنت واحتفظوا برمز المتابعة."},
            {"t": "دراسة المديرية التنفيذية", "d": "تدرس المديرية التنفيذية الوطنية ملفكم."},
            {"t": "رأي مجلس الإدارة", "d": "يبدي مجلس الإدارة رأيه كتابة في قبول الانخراط."},
            {"t": "قرار الجمعية العامة", "d": "تبت الجمعية العامة في الانخراط."},
        ],
        "news_home_title": "آخر الأخبار",
        "founders_title": "المنظمات المؤسسة",
        "cta_title": "هل تربي هيكلكم أطفالا؟",
        "cta_text": "انضموا إلى الاتحاد الذي يحمل صوت التعليم الإسلامي في كوت ديفوار.",

        # ---- à propos ----
        "desc_apropos": "تاريخ منصة الهياكل الإسلامية للتعليم وموضوعها ومهامها ومبادئها.",
        "about_title": "عن المنصة",
        "about_lead": "اتحاد وُلد من إرادة المنظمات الإسلامية للتعليم في التحدث بصوت واحد.",
        "story_title": "تاريخنا",
        "story": [
            "في 3 سبتمبر 2021 اجتمعت المنظمات والجمعيات الإسلامية للتعليم في كوت ديفوار في جمعية عامة تأسيسية، وقررت إنشاء هيكل جمعوي ذي طابع اتحادي لتوجيه وتنسيق المنظمات الإسلامية للتعليم.",
            "تمت مراجعة النظام الأساسي سنة 2026 لتعزيز الحوكمة: مجلس الإدارة والمديرية التنفيذية الوطنية ومفوضية الحسابات واللجان التقنية الدائمة.",
        ],
        "object_title": "موضوعنا",
        "object": ("تنسيق وتمثيل المنظمات الوطنية للتعليم الإسلامي في علاقاتها مع دولة كوت ديفوار والشركاء التقنيين والماليين "
                   "في مجال التعليم، من أجل ترقية تعليم إسلامي منظم وعصري ومتوافق مع القيم الجمهورية."),
        "context_title": "إطار قانوني والتزام",
        "context": [
            "المنصة منظمة من المجتمع المدني غير ربحية، غير سياسية وغير طائفية، يحكمها الأمر رقم 2024-368 المؤرخ في 12 يونيو 2024.",
            "تندرج في سياسة التمدرس الإجباري (القانون رقم 2015-635 المؤرخ في 17 سبتمبر 2015) وفي هدف إدماج الهياكل الإسلامية للتعليم في المنظومة التعليمية النظامية.",
            "تعتبر التعليم حقا أساسيا لكل طفل وتعمل من أجل مصلحته الفضلى.",
        ],

        # ---- gouvernance ----
        "desc_gouvernance": "هيئات المنصة: الجمعية العامة ومجلس الإدارة والمديرية التنفيذية الوطنية ومفوضية الحسابات واللجان والتمثيليات الجهوية.",
        "gov_title": "الحوكمة",
        "gov_lead": "أربع هيئات ولجنتان تقنيتان وشبكة جهوية: تنظيم جماعي خاضع للمراقبة وشفاف.",
        "chart_ag": "الجمعية العامة", "chart_ag_sub": "الهيئة العليا",
        "chart_ca": "مجلس الإدارة", "chart_ca_sub": "13 عضوا",
        "chart_cc": "مفوضية الحسابات", "chart_cc_sub": "مفوضان",
        "chart_den": "المديرية التنفيذية الوطنية", "chart_den_sub": "هيئة التنفيذ",
        "chart_com": "اللجان التقنية", "chart_com_sub": "CNECI · CNVSP",
        "chart_reg": "التمثيليات الجهوية", "chart_reg_sub": "41 مديرية",
        "organs": [
            {"name": "الجمعية العامة", "tag": "الهيئة العليا", "points": [
                "تتكون من أعضاء مجلس الإدارة ومفوضية الحسابات والمديرية التنفيذية الوطنية والمنظمات الأعضاء.",
                "سنوية (الأنشطة والتقارير والميزانية) أو عادية كل ثلاث سنوات (التوجهات وانتخاب الهيئات) أو استثنائية (النظام الأساسي والحل).",
                "يتم استدعاؤها قبل خمسة عشر يوما على الأقل، وتتداول بصفة صحيحة بحضور ثلثي أعضائها.",
            ]},
            {"name": "مجلس الإدارة", "tag": "المراقبة والإشراف", "points": [
                "ثلاثة عشر عضوا من المنظمات الست المؤسسة (اثنان عن كل منظمة)، بولاية مدتها ثلاث سنوات.",
                "يسهر على تنفيذ قرارات الجمعية العامة ويشرف على تسيير المديرية التنفيذية.",
                "يبدي رأيا مكتوبا في قبول عضو أو تعليق عضويته وفي جدول أعمال الجمعيات.",
            ]},
            {"name": "المديرية التنفيذية الوطنية", "tag": "هيئة التنفيذ", "points": [
                "يديرها المدير التنفيذي الوطني، مع ست أمانات، لكل منها نائب.",
                "الإدارة والشؤون القانونية؛ التكوين والبيداغوجيا ومتابعة البرامج؛ الامتحانات والمسابقات والحياة اللاصفية.",
                "الشؤون المالية وتعبئة الموارد؛ الإعلام والاتصال والعلاقات العامة؛ إدماج المدارس والموارد البشرية.",
            ]},
            {"name": "مفوضية الحسابات", "tag": "المراقبة المالية", "points": [
                "مفوضان تنتخبهما الجمعية العامة لمدة ثلاث سنوات.",
                "اطلاع على كل القيود والوثائق المحاسبية وحالة الصندوق عند كل طلب.",
                "تقرير مكتوب بعد كل تحقيق؛ ويمكنها استدعاء جمعية عامة استثنائية عند وجود تسيير فعلي غير قانوني.",
            ]},
        ],
        "commissions_title": "اللجان التقنية الدائمة",
        "commissions": [
            {"sigle": "CNECI", "name": "اللجنة الوطنية للامتحانات والمسابقات الإسلامية", "points": [
                "تراجع وتصادق على اختبارات الامتحانات الإسلامية الكبرى.",
                "تجمع الإحصاءات وتقترح مواعيد الامتحانات.",
                "توفر الوثائق الموحدة: الشهادة وكشوف النقاط والإفادات.",
            ]},
            {"sigle": "CNVSP", "name": "اللجنة الوطنية لاعتماد الكتب ومتابعة البرامج", "points": [
                "تسهر على تطبيق البرنامج والتوقيت الزمني الموحدين.",
                "تراقب وتصادق وتنشر قائمة الكتب المدرسية المعتمدة.",
                "تشترط تعاون كل مؤلف أو ناشر مع منظمة عضو.",
            ]},
        ],
        "regional_title": "شبكة في كل الجهات",
        "regional": ("تتمثل المنصة في كل مديرية جهوية للتربية الوطنية بمندوب جهوي، "
                     "وهي حاليا في 41 مديرية. ويؤمن مندوبو الدوائر الواجهة المحلية في التعليم التحضيري والابتدائي."),
        "transparency_title": "الشفافية والامتثال",
        "transparency": [
            "السنة المالية من فاتح يناير إلى 31 ديسمبر؛ وتوضع القوائم المالية رهن الإشارة قبل خمسة عشر يوما على الأقل من الجمعية العامة.",
            "توقيع مزدوج إلزامي لسحب الأموال، من مسؤولين ينتميان إلى منظمتين مختلفتين.",
            "سجل للهبات يبين هوية المتبرع والتاريخ والطبيعة والمبلغ؛ والتزام بمكافحة غسل الأموال.",
            "تصريح أعضاء الهيئات بتضارب المصالح؛ والوظائف تمارس تطوعا.",
        ],

        # ---- membres ----
        "desc_membres": "المنظمات الأعضاء في المنصة وشروط الانخراط.",
        "members_title": "أعضاؤنا",
        "members_lead": "منظمات إسلامية للتعليم اجتمعت لتحمل معا صوت هياكلها.",
        "categories_title": "فئات الأعضاء",
        "categories": [
            {"t": "الأعضاء المؤسسون", "d": "المنظمات التي كانت وراء إنشاء المنصة والممثلة في الجمعية العامة التأسيسية."},
            {"t": "الأعضاء العاديون", "d": "المنظمات المسؤولة عن هياكل إسلامية للتعليم، المؤسسة قانونا، والتي تنخرط في النظام الأساسي."},
            {"t": "أعضاء الشرف", "d": "الأشخاص أو المؤسسات التي تعترف لها الجمعية العامة بهذه الصفة."},
        ],
        "founders": ["OEECI", "LECIM", "IQRA", "CHERIFLA", "AL HIKMA", "HINNEH"],

        # ---- adhésion ----
        "desc_adhesion": "شروط وخطوات الانخراط في المنصة.",
        "join_title": "الانخراط في المنصة",
        "join_lead": "هل أنتم منظمة مسؤولة عن هياكل إسلامية للتعليم؟ انضموا إلى الاتحاد.",
        "conditions_title": "من يمكنه الانخراط؟",
        "conditions_intro": "يمكن للمنظمات الإسلامية للتعليم المؤسسة قانونا أن تنخرط إذا:",
        "conditions": [
            "وافقت على النظام الأساسي للمنصة؛",
            "سددت رسم الانخراط؛",
            "التزمت بدفع اشتراكاتها بانتظام؛",
            "استوفت متطلبات وإجراءات الانخراط.",
        ],
        "process_title": "مسار طلبكم",
        "process_note": "تحدد هيئات المنصة مبلغ رسم الانخراط والاشتراكات. يرجى الاستفسار لدى الأمانة.",
        "join_online": "تقديم طلبي عبر الإنترنت",
        "join_track_text": "هل قدمتم طلبا من قبل؟ تابعوا تقدمه برمزكم.",

        # ---- vérification ----
        "desc_verification": "التحقق من صحة إيصال أو شهادة أو وثيقة صادرة عن المنصة.",
        "verify_title": "التحقق من وثيقة",
        "verify_lead": "تحمل إيصالات المنصة وشهادات الاشتراك وشهادات الانخراط رمزا مربعا (QR) يتيح التحقق من صحتها.",
        "verify_steps": [
            "امسحوا الرمز المطبوع على الوثيقة بكاميرا هاتفكم.",
            "تفتح صفحة التحقق على الموقع الآمن للمنصة.",
            "تأكدوا من أن الرقم والمنظمة والمبلغ تطابق الوثيقة التي بحوزتكم.",
        ],
        "verify_note": "يتم التنبيه في صفحة التحقق إلى الإيصال الملغى أو الشهادة التي لم تعد سارية.",

        # ---- FAQ ----
        "desc_faq": "أسئلة شائعة حول المنصة والانخراط والتحقق من الوثائق.",
        "faq_title": "أسئلة شائعة",
        "faq": [
            {"q": "ما هي المنصة؟", "a": "اتحاد ينسق ويمثل المنظمات الوطنية للتعليم الإسلامي في كوت ديفوار لدى الدولة وشركاء التعليم."},
            {"q": "من يمكنه الانخراط؟", "a": "كل منظمة إسلامية للتعليم مؤسسة قانونا توافق على النظام الأساسي وتسدد رسم الانخراط وتلتزم بالاشتراك بانتظام."},
            {"q": "كيف أنخرط؟", "a": "بتقديم طلب عبر الإنترنت. تدرسه المديرية التنفيذية الوطنية ويعرض على مجلس الإدارة لإبداء رأيه كتابة ثم تبت فيه الجمعية العامة."},
            {"q": "كم تبلغ تكلفة الانخراط؟", "a": "تحدد هيئات المنصة رسم الانخراط والاشتراكات. اتصلوا بالأمانة لمعرفة المبالغ المعمول بها."},
            {"q": "كيف أتابع طلبي؟", "a": "برمز المتابعة الذي تسلمتموه عند تقديم الطلب، في صفحة «متابعة طلبي»."},
            {"q": "كيف أتحقق من إيصال أو شهادة؟", "a": "بمسح رمزها المربع: تؤكد صفحة التحقق صحة الوثيقة."},
            {"q": "من يدير المنصة؟", "a": "يتولى التنفيذ مدير تنفيذي وطني وست أمانات، ويشرف عليهم مجلس إدارة من ثلاثة عشر عضوا، ويراقب مفوضان الحسابات."},
            {"q": "أين يوجد المقر؟", "a": "في أبيدجان، بلدية تريشفيل، داخل مسجد الفتح، الشارع 8، الزقاق 15."},
        ],

        # ---- contact ----
        "desc_contact": "بيانات الاتصال بمقر المنصة في أبيدجان.",
        "contact_title": "اتصل بنا",
        "contact_lead": "للحصول على معلومات حول المنصة أو الانخراط، اتصلوا بالأمانة.",
        "contact_note": "يمكنكم أيضا تقديم طلب انخراط مباشرة عبر الإنترنت.",

        # ---- mentions légales ----
        "desc_mentions": "الإشعارات القانونية والخصوصية لموقع المنصة.",
        "legal_title": "الإشعارات القانونية والخصوصية",
        "legal": [
            {"t": "ناشر الموقع", "p": [
                "منصة الهياكل الإسلامية للتعليم، منظمة من المجتمع المدني غير ربحية يحكمها الأمر رقم 2024-368 المؤرخ في 12 يونيو 2024.",
                "المقر: مسجد الفتح، الشارع 8، الزقاق 15، تريشفيل، أبيدجان. مدير النشر: المدير التنفيذي الوطني."]},
            {"t": "الاستضافة", "p": ["يُستضاف الموقع على خدمة GitHub Pages. أما تطبيق الانخراط والإدارة فيُستضاف على خادم مستقل."]},
            {"t": "ملفات تعريف الارتباط وقياس الجمهور", "p": ["لا يضع هذا الموقع أي ملف تعريف ارتباط ولا يستخدم أي أداة لقياس الجمهور أو للإعلانات."]},
            {"t": "البيانات الشخصية", "p": [
                "لا يجمع هذا الموقع أي بيانات شخصية. المعلومات المدخلة في طلب الانخراط تدخل في تطبيق المنصة وتُستعمل فقط لدراسة هذا الطلب.",
                "قوائم الأعضاء والأخبار المعروضة قادمة من التطبيق ولا تتضمن إلا معلومات عامة."]},
            {"t": "المحتوى", "p": ["تعرض النصوص النظام الأساسي للمنصة. وعند أي اختلاف، يُعتمد النظام الأساسي."]},
        ],
    },
}


# ---- ressources : documents, régions, galerie, fiches des faîtières, mot du Président ----
T["fr"].update({
    "announce": "Annonce", "close": "Fermer",
    "nav_docs": "Documents", "nav_regions": "Représentations régionales", "nav_gallery": "Galerie",
    "desc_documents": "Statuts, règlement intérieur et documents officiels de la PSIE à télécharger.",
    "docs_title": "Documents officiels", "docs_lead": "Les textes et formulaires de la PSIE, à télécharger.",
    "docs_empty": "Les documents seront bientôt disponibles.", "download": "Télécharger",
    "desc_regions": "Les représentations régionales de la PSIE auprès des Directions Régionales de l'Éducation Nationale (DRENA).",
    "regions_title": "Représentations régionales",
    "regions_lead": "La PSIE est représentée auprès des Directions Régionales de l'Éducation Nationale par un délégué régional.",
    "regions_empty": "La liste des représentations régionales sera bientôt publiée.",
    "regions_search": "Rechercher une DRENA, une région ou un délégué", "regions_count": "{n} représentations régionales", "delegate": "Délégué",
    "desc_galerie": "Photos des activités et des événements de la PSIE.",
    "gallery_title": "Galerie", "gallery_lead": "Les moments forts de la vie de la fédération.",
    "gallery_empty": "Les photos seront bientôt disponibles.",
    "president_title": "Le mot du Président",
    "fa_about": "Présentation", "fa_facts": "En bref", "fa_status": "Statut", "fa_founded": "Création", "fa_schools": "Structures d'éducation",
    "fa_address": "Adresse", "fa_phone": "Téléphone", "fa_email": "E-mail", "fa_website": "Site web", "fa_back": "Tous nos membres",
    "fa_empty": "La présentation de cette organisation sera bientôt publiée.",
})
T["ar"].update({
    "announce": "إعلان", "close": "إغلاق",
    "nav_docs": "الوثائق", "nav_regions": "التمثيليات الجهوية", "nav_gallery": "معرض الصور",
    "desc_documents": "النظام الأساسي والنظام الداخلي والوثائق الرسمية للمنصة للتحميل.",
    "docs_title": "الوثائق الرسمية", "docs_lead": "نصوص ونماذج المنصة للتحميل.",
    "docs_empty": "ستتوفر الوثائق قريبا.", "download": "تحميل",
    "desc_regions": "التمثيليات الجهوية للمنصة لدى المديريات الجهوية للتربية الوطنية.",
    "regions_title": "التمثيليات الجهوية",
    "regions_lead": "تتمثل المنصة لدى المديريات الجهوية للتربية الوطنية بمندوب جهوي.",
    "regions_empty": "ستنشر قائمة التمثيليات الجهوية قريبا.",
    "regions_search": "ابحث عن مديرية أو جهة أو مندوب", "regions_count": "{n} تمثيلية جهوية", "delegate": "المندوب",
    "desc_galerie": "صور أنشطة وفعاليات المنصة.",
    "gallery_title": "معرض الصور", "gallery_lead": "أبرز لحظات حياة الاتحاد.",
    "gallery_empty": "ستتوفر الصور قريبا.",
    "president_title": "كلمة الرئيس",
    "fa_about": "تقديم", "fa_facts": "نبذة", "fa_status": "الصفة", "fa_founded": "سنة التأسيس", "fa_schools": "الهياكل التعليمية",
    "fa_address": "العنوان", "fa_phone": "الهاتف", "fa_email": "البريد الإلكتروني", "fa_website": "الموقع الإلكتروني", "fa_back": "جميع الأعضاء",
    "fa_empty": "سيتم نشر تقديم هذه المنظمة قريبا.",
})

T["fr"].update({
    "map_tools": "Commandes de la carte", "map_zoom_in": "Zoomer", "map_zoom_out": "Dézoomer", "map_reset": "Recentrer la carte",
    "map_hint": "Glissez pour déplacer, Ctrl + molette ou deux doigts pour zoomer, cliquez sur un point pour voir la DRENA.",
    "map_close": "Fermer", "map_here": "DRENA à cet endroit",
})
T["ar"].update({
    "map_tools": "أدوات الخريطة", "map_zoom_in": "تكبير", "map_zoom_out": "تصغير", "map_reset": "إعادة توسيط الخريطة",
    "map_hint": "اسحب للتحريك، Ctrl + عجلة الفأرة أو إصبعان للتكبير، انقر على نقطة لعرض المديرية.",
    "map_close": "إغلاق", "map_here": "المديريات في هذا الموقع",
})
