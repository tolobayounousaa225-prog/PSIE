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
    ("transparence", "nav_transparency", True),
    ("partenariat", "nav_partnership", True),
    ("guide", "nav_guide", True),
    ("statuts", "nav_rules", True),
    ("affiche", "nav_poster", True),
    ("equipe", "nav_team", True),
    ("partenaires", "nav_partners", True),
    ("glossaire", "nav_glossary", True),
    ("confidentialite", "nav_privacy", True),
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

T["fr"].update({
    "map_attribution": "© contributeurs OpenStreetMap", "map_labels": "Noms des DRENA affichés à partir d'un certain zoom.",
    "map_unavailable": "La carte n'a pas pu être chargée. La liste des DRENA reste disponible ci-contre.",
})
T["ar"].update({
    "map_attribution": "© مساهمو OpenStreetMap", "map_labels": "تظهر أسماء المديريات عند التكبير.",
    "map_unavailable": "تعذر تحميل الخريطة. تبقى قائمة المديريات متاحة بجانبها.",
})
T["fr"]["map_hint"] = "Glissez pour déplacer, Ctrl + molette ou deux doigts pour zoomer, cliquez sur un point pour voir la DRENA."


# ---- histoire, bureau, partenaires, glossaire, confidentialité, 404, réseaux ----
T["fr"].update({
    "nav_team": "Bureau exécutif", "nav_partners": "Partenaires", "nav_glossary": "Glossaire", "nav_privacy": "Confidentialité",
    "footer_discover": "Découvrir", "footer_help": "Aide", "footer_legal": "Informations légales", "follow_us": "Suivez-nous",
    "social_names": {"facebook": "Facebook", "youtube": "YouTube", "instagram": "Instagram"},
    "whatsapp_cta": "Nous écrire sur WhatsApp",
    "timeline_title": "Les grandes étapes", "timeline_lead": "Du cadre légal à la fédération d'aujourd'hui.",
    "timeline": [
        {"date": "17 septembre 2015", "t": "Scolarisation obligatoire",
         "d": "La loi n° 2015-635 rend l'école obligatoire : c'est dans cette politique que s'inscrit l'action de la PSIE."},
        {"date": "3 septembre 2021", "t": "Assemblée Générale Constitutive",
         "d": "Les organisations et associations islamiques d'éducation décident de créer une structure fédérative pour l'orientation et la coordination."},
        {"date": "12 juin 2024", "t": "Ordonnance n° 2024-368",
         "d": "Le cadre légal qui régit la PSIE, organisation de la société civile à but non lucratif, apolitique et non sectaire."},
        {"date": "2026", "t": "Révision des statuts",
         "d": "Mise en place du Conseil d'Administration, de la Direction Exécutive Nationale, du Commissariat aux Comptes et des commissions techniques permanentes."},
    ],
    "desc_equipe": "Les responsables de la Direction Exécutive Nationale, du Conseil d'Administration et du Commissariat aux Comptes de la PSIE.",
    "team_title": "Bureau exécutif", "team_lead": "Celles et ceux qui animent la fédération au quotidien.",
    "team_empty": "La présentation du bureau sera bientôt publiée.",
    "team_groups": {"den": "Direction Exécutive Nationale", "ca": "Conseil d'Administration", "cc": "Commissariat aux Comptes"},
    "desc_partenaires": "L'État, les partenaires techniques et financiers qui accompagnent la PSIE.",
    "partners_title": "Partenaires", "partners_lead": "Ils soutiennent l'éducation islamique structurée en Côte d'Ivoire.",
    "partners_empty": "La liste des partenaires sera bientôt publiée.",
    "partner_types": {"etat": "L'État et ses services", "technique": "Partenaires techniques", "financier": "Partenaires financiers"},
    "visit_site": "Visiter le site",
    "desc_glossaire": "Les sigles et les mots clés de la PSIE expliqués simplement.",
    "glossary_title": "Glossaire", "glossary_lead": "Les sigles et les mots que vous croiserez sur ce site, expliqués simplement.",
    "glossary": [
        {"term": "PSIE", "full": "Plateforme des Structures Islamiques d'Éducation", "d": "La fédération qui coordonne et représente les organisations nationales islamiques d'éducation de Côte d'Ivoire."},
        {"term": "Faîtière", "full": "Organisation nationale", "d": "Organisation qui regroupe plusieurs écoles ou structures d'éducation. La PSIE réunit six faîtières fondatrices."},
        {"term": "AG", "full": "Assemblée Générale", "d": "L'organe suprême de la PSIE. Elle est annuelle, ordinaire (tous les trois ans) ou extraordinaire."},
        {"term": "AGA", "full": "Assemblée Générale Annuelle", "d": "Elle examine chaque année les activités, les rapports et le budget."},
        {"term": "AGE", "full": "Assemblée Générale Extraordinaire", "d": "Elle décide des changements des statuts et de la dissolution."},
        {"term": "CA", "full": "Conseil d'Administration", "d": "Treize administrateurs issus des six organisations fondatrices, pour un mandat de trois ans. Il supervise la gestion de la Direction Exécutive."},
        {"term": "DEN", "full": "Direction Exécutive Nationale", "d": "L'organe d'exécution, dirigé par le Directeur Exécutif National avec six secrétariats."},
        {"term": "CC", "full": "Commissariat aux Comptes", "d": "Deux commissaires qui contrôlent les écritures, les pièces comptables et l'état de caisse."},
        {"term": "CNECI", "full": "Commission Nationale des Examens et Concours Islamiques", "d": "Vérifie et valide les épreuves des examens islamiques, et propose les calendriers."},
        {"term": "CNVSP", "full": "Commission Nationale de Validation des Manuels et du Suivi des Programmes", "d": "Contrôle, valide et publie la liste des manuels scolaires homologués."},
        {"term": "DRENA", "full": "Direction Régionale de l'Éducation Nationale et de l'Alphabétisation", "d": "Le service régional de l'État. La PSIE est représentée auprès de chacune par un délégué régional."},
        {"term": "Quorum", "full": "Présence minimale", "d": "Nombre minimal de membres présents pour que l'assemblée puisse décider : ici, les deux tiers."},
        {"term": "Droit d'adhésion", "full": "", "d": "Somme versée une fois par une organisation qui rejoint la PSIE."},
        {"term": "Cotisation", "full": "Annuelle ou exceptionnelle", "d": "Contribution des membres au fonctionnement de la fédération. Elle est annuelle ; une cotisation exceptionnelle peut être décidée par les organes."},
        {"term": "Double signature", "full": "", "d": "Tout retrait de fonds exige la signature de deux responsables issus d'organisations différentes."},
    ],
    "desc_confidentialite": "Ce que le site de la PSIE collecte, et ce qu'il ne collecte pas.",
    "privacy_title": "Confidentialité", "privacy_lead": "Ce site respecte votre vie privée : voici, en clair, ce qui se passe quand vous le visitez.",
    "privacy": [
        {"t": "Ce que nous ne collectons pas", "p": ["Le site ne vous demande aucun nom, aucune adresse e-mail, aucun mot de passe. Il ne dépose aucun cookie et n'affiche aucune publicité."]},
        {"t": "Les demandes d'adhésion", "p": ["Les informations d'une demande d'adhésion sont saisies sur l'application de la PSIE (et non sur ce site). Elles servent uniquement à instruire la demande."]},
        {"t": "La carte des représentations régionales", "p": ["Pour afficher la carte, votre navigateur charge le fond de carte depuis OpenStreetMap, comme tout site utilisant cette carte. Votre adresse IP est alors visible de ce service. Aucun autre site n'est contacté."]},
        {"t": "Liens vers d'autres sites", "p": ["Les fiches des organisations membres peuvent renvoyer vers leurs propres sites. Leurs règles de confidentialité leur appartiennent."]},
        {"t": "Hébergement", "p": ["Le site est hébergé par GitHub Pages, qui conserve des journaux techniques de connexion selon sa propre politique."]},
        {"t": "Vos droits", "p": ["Pour toute question sur vos données, écrivez au secrétariat (voir la page Contact). Vous pouvez demander l'accès, la correction ou la suppression des informations que la PSIE détient sur vous."]},
    ],
    "privacy_stats_off": {"t": "Mesure d'audience", "p": ["Ce site n'utilise aucun outil de mesure d'audience."]},
    "privacy_stats_on": {"t": "Mesure d'audience", "p": ["Pour savoir combien de personnes visitent le site, nous utilisons GoatCounter, un outil qui ne dépose aucun cookie et ne vous identifie pas. Il enregistre seulement les pages vues, le pays, le type d'appareil et la langue, sous forme de statistiques anonymes."]},
    "desc_404": "Page introuvable.",
    "notfound_title": "Page introuvable", "notfound_text": "L'adresse que vous avez saisie n'existe pas ou a changé. Voici des liens pour retrouver votre chemin.",
    "notfound_home": "Retour à l'accueil", "notfound_ar": "الصفحة غير موجودة. يمكنكم العودة إلى الصفحة الرئيسية.",
})
T["ar"].update({
    "nav_team": "المكتب التنفيذي", "nav_partners": "الشركاء", "nav_glossary": "المصطلحات", "nav_privacy": "الخصوصية",
    "footer_discover": "اكتشف", "footer_help": "مساعدة", "footer_legal": "معلومات قانونية", "follow_us": "تابعونا",
    "social_names": {"facebook": "فيسبوك", "youtube": "يوتيوب", "instagram": "إنستغرام"},
    "whatsapp_cta": "راسلونا على واتساب",
    "timeline_title": "المحطات الكبرى", "timeline_lead": "من الإطار القانوني إلى الاتحاد اليوم.",
    "timeline": [
        {"date": "17 شتنبر 2015", "t": "إلزامية التمدرس",
         "d": "القانون رقم 2015-635 يجعل التمدرس إلزاميا، وفي هذه السياسة يندرج عمل المنصة."},
        {"date": "3 شتنبر 2021", "t": "الجمعية العامة التأسيسية",
         "d": "قررت المنظمات والجمعيات الإسلامية للتعليم إنشاء هيكل اتحادي للتوجيه والتنسيق."},
        {"date": "12 يونيو 2024", "t": "الأمر رقم 2024-368",
         "d": "الإطار القانوني الذي ينظم المنصة، وهي منظمة من المجتمع المدني غير ربحية وغير سياسية وغير طائفية."},
        {"date": "2026", "t": "مراجعة النظام الأساسي",
         "d": "إحداث مجلس الإدارة والإدارة التنفيذية الوطنية ومفوضية الحسابات واللجان التقنية الدائمة."},
    ],
    "desc_equipe": "مسؤولو الإدارة التنفيذية الوطنية ومجلس الإدارة ومفوضية الحسابات في المنصة.",
    "team_title": "المكتب التنفيذي", "team_lead": "من يسيّرون الاتحاد يوميا.",
    "team_empty": "سيتم نشر تقديم المكتب قريبا.",
    "team_groups": {"den": "الإدارة التنفيذية الوطنية", "ca": "مجلس الإدارة", "cc": "مفوضية الحسابات"},
    "desc_partenaires": "الدولة والشركاء التقنيون والماليون الذين يرافقون المنصة.",
    "partners_title": "الشركاء", "partners_lead": "يدعمون التعليم الإسلامي المنظم في كوت ديفوار.",
    "partners_empty": "ستنشر قائمة الشركاء قريبا.",
    "partner_types": {"etat": "الدولة ومصالحها", "technique": "الشركاء التقنيون", "financier": "الشركاء الماليون"},
    "visit_site": "زيارة الموقع",
    "desc_glossaire": "اختصارات المنصة ومصطلحاتها الأساسية بعبارات بسيطة.",
    "glossary_title": "المصطلحات", "glossary_lead": "الاختصارات والكلمات التي ستصادفونها في هذا الموقع، موضحة ببساطة.",
    "glossary": [
        {"term": "PSIE", "full": "منصة الهياكل الإسلامية للتعليم", "d": "الاتحاد الذي ينسق ويمثل المنظمات الوطنية للتعليم الإسلامي في كوت ديفوار."},
        {"term": "الهيئة الجامعة", "full": "منظمة وطنية", "d": "منظمة تضم عدة مدارس أو هياكل تعليمية. تجمع المنصة ست هيئات مؤسسة."},
        {"term": "AG", "full": "الجمعية العامة", "d": "الهيئة العليا للمنصة. وقد تكون سنوية أو عادية (كل ثلاث سنوات) أو استثنائية."},
        {"term": "AGA", "full": "الجمعية العامة السنوية", "d": "تدرس كل سنة الأنشطة والتقارير والميزانية."},
        {"term": "AGE", "full": "الجمعية العامة الاستثنائية", "d": "تقرر تعديل النظام الأساسي والحل."},
        {"term": "CA", "full": "مجلس الإدارة", "d": "ثلاثة عشر عضوا من المنظمات الست المؤسسة، لولاية مدتها ثلاث سنوات. يشرف على تسيير الإدارة التنفيذية."},
        {"term": "DEN", "full": "الإدارة التنفيذية الوطنية", "d": "هيئة التنفيذ، يديرها المدير التنفيذي الوطني مع ست أمانات."},
        {"term": "CC", "full": "مفوضية الحسابات", "d": "مفوضان يراقبان القيود والوثائق المحاسبية وحالة الصندوق."},
        {"term": "CNECI", "full": "اللجنة الوطنية للامتحانات والمباريات الإسلامية", "d": "تتحقق من اختبارات الامتحانات الإسلامية وتصادق عليها، وتقترح الجداول."},
        {"term": "CNVSP", "full": "اللجنة الوطنية لاعتماد الكتب ومتابعة البرامج", "d": "تراقب الكتب المدرسية وتعتمدها وتنشر قائمتها."},
        {"term": "DRENA", "full": "المديرية الجهوية للتربية الوطنية ومحو الأمية", "d": "المصلحة الجهوية للدولة. تتمثل المنصة لدى كل منها بمندوب جهوي."},
        {"term": "النصاب", "full": "الحد الأدنى للحضور", "d": "العدد الأدنى من الأعضاء الحاضرين ليتمكن الاجتماع من اتخاذ القرار: هنا الثلثان."},
        {"term": "رسم الانخراط", "full": "", "d": "مبلغ يدفع مرة واحدة من المنظمة التي تنضم إلى المنصة."},
        {"term": "الاشتراك", "full": "سنوي أو استثنائي", "d": "مساهمة الأعضاء في تسيير الاتحاد. هو سنوي، ويمكن للهيئات تقرير اشتراك استثنائي."},
        {"term": "التوقيع المزدوج", "full": "", "d": "كل سحب للأموال يتطلب توقيع مسؤولين من منظمتين مختلفتين."},
    ],
    "desc_confidentialite": "ما يجمعه موقع المنصة وما لا يجمعه.",
    "privacy_title": "الخصوصية", "privacy_lead": "يحترم هذا الموقع خصوصيتكم: إليكم بوضوح ما يحدث عند زيارته.",
    "privacy": [
        {"t": "ما لا نجمعه", "p": ["لا يطلب الموقع منكم أي اسم أو بريد إلكتروني أو كلمة مرور. ولا يضع أي ملف تعريف ارتباط ولا يعرض أي إعلان."]},
        {"t": "طلبات الانخراط", "p": ["تُدخل معلومات طلب الانخراط في تطبيق المنصة (وليس في هذا الموقع). وتُستعمل فقط للنظر في الطلب."]},
        {"t": "خريطة التمثيليات الجهوية", "p": ["لعرض الخريطة، يحمّل متصفحكم خلفية الخريطة من OpenStreetMap، كأي موقع يستعمل هذه الخريطة. ويظهر عندئذ عنوان IP الخاص بكم لهذه الخدمة. ولا يتم الاتصال بأي موقع آخر."]},
        {"t": "روابط نحو مواقع أخرى", "p": ["قد تحيل صفحات المنظمات الأعضاء إلى مواقعها الخاصة، وسياسة الخصوصية فيها تخصها."]},
        {"t": "الاستضافة", "p": ["يُستضاف الموقع لدى GitHub Pages، التي تحتفظ بسجلات اتصال تقنية وفق سياستها الخاصة."]},
        {"t": "حقوقكم", "p": ["لأي سؤال حول بياناتكم، راسلوا الأمانة (انظر صفحة اتصل بنا). يمكنكم طلب الاطلاع على المعلومات التي تحتفظ بها المنصة عنكم أو تصحيحها أو حذفها."]},
    ],
    "privacy_stats_off": {"t": "قياس الزيارات", "p": ["لا يستعمل هذا الموقع أي أداة لقياس الزيارات."]},
    "privacy_stats_on": {"t": "قياس الزيارات", "p": ["لمعرفة عدد زوار الموقع نستعمل GoatCounter، وهي أداة لا تضع ملفات تعريف الارتباط ولا تحدد هويتكم. تسجل فقط الصفحات المعروضة والبلد ونوع الجهاز واللغة في شكل إحصاءات مجهولة."]},
    "desc_404": "الصفحة غير موجودة.",
    "notfound_title": "الصفحة غير موجودة", "notfound_text": "العنوان الذي أدخلتموه غير موجود أو تغيّر. إليكم روابط لاستعادة طريقكم.",
    "notfound_home": "العودة إلى الصفحة الرئيسية", "notfound_ar": "الصفحة غير موجودة. يمكنكم العودة إلى الصفحة الرئيسية.",
})

T["fr"]["legal_cookies_on"] = {"t": "Cookies et mesure d'audience", "p": ["Ce site ne dépose aucun cookie. Il mesure son audience avec GoatCounter, un outil sans cookie qui ne vous identifie pas (voir la page Confidentialité)."]}
T["ar"]["legal_cookies_on"] = {"t": "ملفات تعريف الارتباط وقياس الزيارات", "p": ["لا يضع هذا الموقع أي ملف تعريف ارتباط. ويقيس زياراته عبر GoatCounter، وهي أداة بلا ملفات ارتباط لا تحدد هويتكم (انظر صفحة الخصوصية)."]}

T["fr"]["sr_content"] = "Contenu de la page"
T["ar"]["sr_content"] = "محتوى الصفحة"


# ---- statuts en bref, questionnaire d'adhésion, affiche et plaquette, graphique, organigramme ----
T["fr"].update({
    "nav_rules": "Les statuts en bref", "nav_poster": "Affiche et plaquette",
    "desc_statuts": "Les règles essentielles de la PSIE en dix points : adhésion, assemblées, contrôle des comptes, dons, discipline.",
    "rules_title": "Les statuts en 10 points", "rules_lead": "Les règles qui font fonctionner la PSIE, expliquées simplement.",
    "rules_note": "Résumé pédagogique : seul le texte officiel des Statuts et du Règlement Intérieur fait foi.",
    "rules": [
        {"i": "flag", "t": "Une fédération à but non lucratif", "d": "La PSIE est une organisation de la société civile, apolitique et non sectaire, régie par l'Ordonnance n° 2024-368 du 12 juin 2024."},
        {"i": "handshake", "t": "Qui peut adhérer ?", "d": "Les organisations islamiques d'éducation légalement constituées qui approuvent les statuts, paient le droit d'adhésion et leurs cotisations. La demande est examinée par la DEN, soumise à l'avis écrit du CA, puis décidée par l'AG."},
        {"i": "users", "t": "L'Assemblée Générale décide", "d": "Organe suprême : annuelle (activités, rapports, budget), ordinaire tous les trois ans (orientations, élection des organes) ou extraordinaire (statuts, dissolution)."},
        {"i": "check", "t": "Convocation et quorum", "d": "L'assemblée est convoquée au moins quinze jours à l'avance et ne délibère valablement qu'en présence des deux tiers de ses membres."},
        {"i": "scale", "t": "Un Conseil d'Administration de treize membres", "d": "Treize administrateurs issus des six organisations fondatrices (deux par structure), pour un mandat de trois ans. Il donne un avis écrit sur les admissions et les suspensions."},
        {"i": "spark", "t": "Une Direction Exécutive pour agir", "d": "Dirigée par le Directeur Exécutif National avec six secrétariats, elle administre, forme, organise les examens, mobilise les ressources et communique."},
        {"i": "shield", "t": "Des comptes contrôlés", "d": "Deux commissaires aux comptes, élus pour trois ans, ont accès à toutes les écritures et pièces. Ils peuvent convoquer une Assemblée Générale Extraordinaire en cas de gestion de fait."},
        {"i": "file", "t": "L'argent sous double signature", "d": "L'exercice va du 1er janvier au 31 décembre. Tout retrait de fonds exige la signature de deux responsables issus d'organisations différentes, et les états financiers sont mis à disposition quinze jours avant l'assemblée."},
        {"i": "book", "t": "Dons et intérêts : la transparence", "d": "Un registre des dons indique le donateur, la date, la nature et le montant, avec un engagement contre le blanchiment de capitaux. Les responsables déclarent leurs conflits d'intérêts et exercent leurs fonctions à titre bénévole."},
        {"i": "pin", "t": "Discipline et dissolution", "d": "Les sanctions sont graduées : avertissement, blâme, suspension, radiation. La dissolution ne peut être décidée qu'en Assemblée Générale Extraordinaire, à la majorité des quatre cinquièmes."},
    ],
    "rules_cta": "Voir le glossaire des sigles",
    "elig_title": "Mon organisation peut-elle adhérer ?", "elig_lead": "Répondez à cinq questions. Le résultat est indicatif : la décision appartient à l'Assemblée Générale.",
    "elig_start": "Commencer", "elig_yes": "Oui", "elig_no": "Non", "elig_progress": "Question {n} sur {total}", "elig_restart": "Recommencer",
    "elig_questions": [
        "Votre organisation est-elle une organisation islamique d'éducation légalement constituée ?",
        "Approuvez-vous les statuts de la PSIE ?",
        "Êtes-vous prêt à vous acquitter du droit d'adhésion ?",
        "Vous engagez-vous à payer régulièrement vos cotisations ?",
        "Êtes-vous prêt à satisfaire aux exigences et formalités d'adhésion ?",
    ],
    "elig_ok_title": "Votre organisation semble remplir les conditions",
    "elig_ok_text": "Préparez ces informations avant de déposer votre demande en ligne :",
    "elig_prepare": ["Le nom et le sigle de l'organisation", "Le nom et la fonction de son représentant", "Une adresse e-mail et un numéro de téléphone",
                     "L'adresse du siège", "Le statut juridique et la date de création", "Le nombre de structures (écoles) de l'organisation"],
    "elig_ko_title": "Il manque encore une condition", "elig_ko_text": "La condition suivante n'est pas remplie :",
    "elig_ko_help": "Contactez le secrétariat : il pourra vous accompagner.", "elig_contact": "Contacter le secrétariat",
    "poster_title": "Affiche et plaquette", "poster_lead": "Des supports prêts à imprimer et à partager, générés automatiquement à partir du site.",
    "desc_affiche": "Affiche avec QR code et plaquette de présentation de la PSIE à télécharger.",
    "poster_heading": "Scannez pour découvrir la PSIE", "poster_version_fr": "Version française", "poster_version_ar": "Version arabe",
    "poster_print": "Imprimer l'affiche", "poster_svg": "QR code (SVG, pour l'impression)", "poster_png": "QR code (PNG)",
    "poster_no_url": "Le QR code sera disponible dès que l'adresse du site sera définie.",
    "brochure_title": "Plaquette de présentation", "brochure_text": "Une page (PDF) avec les missions, les chiffres clés, les organisations fondatrices et les contacts.",
    "brochure_fr": "Télécharger en français (PDF)", "brochure_ar": "Télécharger en arabe (PDF)",
    "bars_title": "Structures d'éducation par organisation", "bars_note": "Chiffres communiqués par chaque organisation, ajoutés au fur et à mesure.", "bars_unit": "structures",
    "chart_hint": "Cliquez sur un organe pour voir son rôle.", "chart_close": "Fermer",
})
T["ar"].update({
    "nav_rules": "النظام الأساسي باختصار", "nav_poster": "الملصق والكتيب",
    "desc_statuts": "القواعد الأساسية للمنصة في عشر نقاط: الانخراط والجمعيات ومراقبة الحسابات والهبات والانضباط.",
    "rules_title": "النظام الأساسي في 10 نقاط", "rules_lead": "القواعد التي تسير بها المنصة، موضحة ببساطة.",
    "rules_note": "ملخص تعليمي: النص الرسمي للنظام الأساسي والنظام الداخلي هو وحده المعتمد.",
    "rules": [
        {"i": "flag", "t": "اتحاد غير ربحي", "d": "المنصة منظمة من المجتمع المدني، غير سياسية وغير طائفية، ينظمها الأمر رقم 2024-368 المؤرخ في 12 يونيو 2024."},
        {"i": "handshake", "t": "من يمكنه الانخراط؟", "d": "المنظمات الإسلامية للتعليم المؤسسة قانونا التي توافق على النظام الأساسي وتدفع رسم الانخراط واشتراكاتها. تدرس الإدارة التنفيذية الوطنية الطلب، ثم يُعرض على رأي مجلس الإدارة الكتابي، وتقرر الجمعية العامة."},
        {"i": "users", "t": "الجمعية العامة تقرر", "d": "الهيئة العليا: سنوية (الأنشطة والتقارير والميزانية)، أو عادية كل ثلاث سنوات (التوجهات وانتخاب الهيئات)، أو استثنائية (النظام الأساسي والحل)."},
        {"i": "check", "t": "الاستدعاء والنصاب", "d": "تُستدعى الجمعية قبل خمسة عشر يوما على الأقل، ولا تتداول بصفة صحيحة إلا بحضور ثلثي أعضائها."},
        {"i": "scale", "t": "مجلس إدارة من ثلاثة عشر عضوا", "d": "ثلاثة عشر عضوا من المنظمات الست المؤسسة (اثنان عن كل هيكل)، لولاية مدتها ثلاث سنوات. يبدي رأيا كتابيا في القبول والتعليق."},
        {"i": "spark", "t": "إدارة تنفيذية للعمل", "d": "يديرها المدير التنفيذي الوطني بمعية ست أمانات، وتتولى التسيير والتكوين وتنظيم الامتحانات وتعبئة الموارد والتواصل."},
        {"i": "shield", "t": "حسابات خاضعة للمراقبة", "d": "مفوضان للحسابات منتخبان لثلاث سنوات، يطلعان على جميع القيود والوثائق، ويمكنهما استدعاء جمعية عامة استثنائية في حال التسيير الفعلي غير القانوني."},
        {"i": "file", "t": "الأموال بتوقيعين", "d": "تمتد السنة المالية من فاتح يناير إلى 31 دجنبر. كل سحب للأموال يتطلب توقيع مسؤولين من منظمتين مختلفتين، وتوضع البيانات المالية رهن الإشارة قبل الجمعية بخمسة عشر يوما."},
        {"i": "book", "t": "الهبات والمصالح: الشفافية", "d": "سجل للهبات يبين المتبرع والتاريخ والطبيعة والمبلغ، مع التزام بمحاربة غسل الأموال. يصرح المسؤولون بتضارب المصالح ويمارسون مهامهم تطوعا."},
        {"i": "pin", "t": "الانضباط والحل", "d": "العقوبات متدرجة: إنذار، توبيخ، تعليق، شطب. ولا يمكن تقرير الحل إلا في جمعية عامة استثنائية بأغلبية أربعة أخماس."},
    ],
    "rules_cta": "اطلع على مسرد الاختصارات",
    "elig_title": "هل يمكن لمنظمتي الانخراط؟", "elig_lead": "أجيبوا عن خمسة أسئلة. النتيجة إرشادية: القرار للجمعية العامة.",
    "elig_start": "ابدأ", "elig_yes": "نعم", "elig_no": "لا", "elig_progress": "السؤال {n} من {total}", "elig_restart": "ابدأ من جديد",
    "elig_questions": [
        "هل منظمتكم منظمة إسلامية للتعليم مؤسسة قانونا؟",
        "هل توافقون على النظام الأساسي للمنصة؟",
        "هل أنتم مستعدون لدفع رسم الانخراط؟",
        "هل تلتزمون بدفع اشتراكاتكم بانتظام؟",
        "هل أنتم مستعدون لاستيفاء شروط الانخراط وإجراءاته؟",
    ],
    "elig_ok_title": "يبدو أن منظمتكم تستوفي الشروط",
    "elig_ok_text": "حضّروا هذه المعلومات قبل إيداع طلبكم عبر الإنترنت:",
    "elig_prepare": ["اسم المنظمة واختصارها", "اسم ممثلها ووظيفته", "بريد إلكتروني ورقم هاتف",
                     "عنوان المقر", "الصفة القانونية وتاريخ التأسيس", "عدد هياكل (مدارس) المنظمة"],
    "elig_ko_title": "ينقص شرط واحد بعد", "elig_ko_text": "الشرط التالي غير مستوفى:",
    "elig_ko_help": "اتصلوا بالأمانة: يمكنها مساعدتكم.", "elig_contact": "الاتصال بالأمانة",
    "poster_title": "الملصق والكتيب", "poster_lead": "مواد جاهزة للطباعة والمشاركة، تُنشأ تلقائيا انطلاقا من الموقع.",
    "desc_affiche": "ملصق برمز QR وكتيب تعريفي بالمنصة للتحميل.",
    "poster_heading": "امسحوا الرمز لاكتشاف المنصة", "poster_version_fr": "النسخة الفرنسية", "poster_version_ar": "النسخة العربية",
    "poster_print": "اطبعوا الملصق", "poster_svg": "رمز QR (SVG للطباعة)", "poster_png": "رمز QR (PNG)",
    "poster_no_url": "سيتوفر رمز QR بمجرد تحديد عنوان الموقع.",
    "brochure_title": "كتيب تعريفي", "brochure_text": "صفحة واحدة (PDF) تضم المهام والأرقام الأساسية والمنظمات المؤسسة وبيانات الاتصال.",
    "brochure_fr": "تحميل بالفرنسية (PDF)", "brochure_ar": "تحميل بالعربية (PDF)",
    "bars_title": "الهياكل التعليمية حسب المنظمة", "bars_note": "أرقام قدمتها كل منظمة، تُضاف تدريجيا.", "bars_unit": "هيكل",
    "chart_hint": "انقروا على هيئة لمعرفة دورها.", "chart_close": "إغلاق",
})

T["fr"]["elig_conditions"] = [
    "Être une organisation islamique d'éducation légalement constituée",
    "Approuver les statuts de la PSIE",
    "S'acquitter du droit d'adhésion",
    "S'engager à payer régulièrement ses cotisations",
    "Satisfaire aux exigences et formalités d'adhésion",
]
T["ar"]["elig_conditions"] = [
    "أن تكون منظمة إسلامية للتعليم مؤسسة قانونا",
    "الموافقة على النظام الأساسي للمنصة",
    "دفع رسم الانخراط",
    "الالتزام بدفع الاشتراكات بانتظام",
    "استيفاء شروط الانخراط وإجراءاته",
]


# ---- centre de transparence, devenir partenaire, guide de l'espace membre ----
T["fr"].update({
    "nav_transparency": "Transparence", "nav_partnership": "Devenir partenaire", "nav_guide": "Guide de l'espace membre",
    "desc_transparence": "Rapports d'activité, états financiers, budgets et procès-verbaux de la PSIE à consulter et à télécharger.",
    "transp_title": "Centre de transparence", "transp_lead": "Rapports, comptes et procès-verbaux de la PSIE, à consulter et à télécharger.",
    "transp_kinds": {"rapport_activite": "Rapports d'activité", "etats_financiers": "États financiers", "budget": "Budgets",
                     "proces_verbal": "Procès-verbaux d'assemblées", "rapport_cc": "Rapports des commissaires aux comptes", "autre": "Autres documents"},
    "transp_all": "Tout", "transp_filter_kind": "Type de document", "transp_filter_year": "Année",
    "transp_empty": "Les premiers documents seront bientôt publiés ici.", "transp_no_match": "Aucun document ne correspond à ce filtre.",
    "transp_commit_lead": "Ce que la PSIE s'engage à rendre public et à contrôler :", "transp_more": "Voir les règles en 10 points",
    "desc_partenariat": "Soutenir l'éducation islamique structurée en Côte d'Ivoire : appui technique, financier, institutionnel ou en nature.",
    "partner_title": "Devenir partenaire de la PSIE", "partner_lead": "Vous souhaitez soutenir l'éducation islamique structurée en Côte d'Ivoire ? Voici comment travailler avec nous.",
    "partner_why_title": "Pourquoi s'associer à la PSIE",
    "partner_why": [
        {"i": "handshake", "t": "Un seul interlocuteur", "d": "Un point d'entrée unique vers les organisations nationales islamiques d'éducation réunies au sein de la fédération."},
        {"i": "shield", "t": "Une gestion contrôlée", "d": "Un Conseil d'Administration, deux commissaires aux comptes, la double signature des retraits et un registre des dons."},
        {"i": "pin", "t": "Une présence dans tout le pays", "d": "Des représentants régionaux auprès des 41 Directions Régionales de l'Éducation Nationale."},
    ],
    "partner_ways_title": "Comment nous soutenir",
    "partner_ways": [
        {"i": "book", "t": "Appui technique", "d": "Formation des enseignants, harmonisation des programmes, organisation des examens, gestion des écoles."},
        {"i": "scale", "t": "Appui financier", "d": "Contribution aux programmes de la fédération. Chaque don est inscrit au registre des dons : donateur, date, nature et montant."},
        {"i": "flag", "t": "Appui institutionnel", "d": "Mise en relation avec l'État et les administrations de l'éducation, pour l'intégration des structures islamiques d'éducation au système formel."},
        {"i": "users", "t": "Appui en nature", "d": "Matériel, équipements ou expertise mis à disposition des écoles et des programmes."},
    ],
    "partner_steps_title": "Comment cela se passe",
    "partner_steps": [
        {"t": "Prenez contact", "d": "Écrivez-nous sur WhatsApp ou appelez le secrétariat."},
        {"t": "Précisons le besoin", "d": "Nous échangeons sur vos objectifs et sur les écoles ou les programmes concernés."},
        {"t": "Formalisons l'appui", "d": "La forme du partenariat est convenue avec les responsables concernés de la PSIE."},
    ],
    "partner_trust": "Vos contributions sont tracées : registre des dons, double signature des retraits et états financiers communiqués aux membres avant l'assemblée.",
    "partner_cta_call": "Appeler le secrétariat", "partner_cta_see": "Voir nos partenaires", "partner_cta_transp": "Consulter le centre de transparence",
    "desc_guide": "Pas à pas : se connecter, suivre ses cotisations, télécharger reçus et attestations, consulter les assemblées, vérifier un document.",
    "guide_title": "Guide de l'espace membre", "guide_lead": "Tout ce que votre organisation peut faire en ligne, pas à pas.",
    "guide_soon": "L'espace en ligne ouvrira prochainement : ce guide vous prépare à son utilisation.", "guide_login": "Se connecter à l'espace membre",
    "guide_steps": [
        {"i": "users", "t": "Se connecter", "d": "Le secrétariat crée le compte du représentant de votre organisation. Connectez-vous avec l'adresse e-mail et le mot de passe remis, puis changez le mot de passe dès la première connexion."},
        {"i": "file", "t": "Consulter la fiche de l'organisation", "d": "Coordonnées, mandats des représentants et situation de vos cotisations."},
        {"i": "scale", "t": "Suivre vos cotisations", "d": "Chaque échéance (cotisation annuelle, droit d'adhésion, cotisation exceptionnelle) affiche le montant dû, le montant payé et le solde."},
        {"i": "check", "t": "Télécharger reçus et attestations", "d": "Chaque paiement donne un reçu en PDF. Une fois la cotisation annuelle soldée, vous téléchargez votre attestation de cotisation."},
        {"i": "book", "t": "Consulter les assemblées", "d": "Convocations en PDF, ordre du jour et procès-verbaux des assemblées convoquées ou tenues."},
        {"i": "qr", "t": "Vérifier un document", "d": "Scannez le QR code d'un reçu, d'une attestation ou d'un certificat d'adhésion : le site confirme s'il est authentique."},
    ],
    "guide_faq_title": "Questions fréquentes",
    "guide_faq": [
        {"q": "Qui peut se connecter ?", "a": "Le représentant désigné par chaque organisation membre, et les responsables des organes de la PSIE selon leur rôle."},
        {"q": "J'ai oublié mon mot de passe.", "a": "Contactez le secrétariat : un administrateur pourra vous aider."},
        {"q": "Les autres organisations voient-elles mes informations ?", "a": "Non. Chaque organisation ne voit que ses propres informations, et les connexions sont protégées."},
        {"q": "Ma demande d'adhésion est-elle suivie ?", "a": "Oui : le code de suivi remis au dépôt permet de consulter l'état de la demande sans compte."},
    ],
    "guide_track": "Suivre ma demande d'adhésion", "guide_verify": "Vérifier un document",
})
T["ar"].update({
    "nav_transparency": "الشفافية", "nav_partnership": "كونوا شركاء", "nav_guide": "دليل فضاء الأعضاء",
    "desc_transparence": "التقارير والبيانات المالية والميزانيات ومحاضر الجمعيات للمنصة للاطلاع والتحميل.",
    "transp_title": "مركز الشفافية", "transp_lead": "تقارير المنصة وحساباتها ومحاضرها، للاطلاع والتحميل.",
    "transp_kinds": {"rapport_activite": "التقارير السنوية", "etats_financiers": "البيانات المالية", "budget": "الميزانيات",
                     "proces_verbal": "محاضر الجمعيات", "rapport_cc": "تقارير مفوضي الحسابات", "autre": "وثائق أخرى"},
    "transp_all": "الكل", "transp_filter_kind": "نوع الوثيقة", "transp_filter_year": "السنة",
    "transp_empty": "ستنشر أولى الوثائق هنا قريبا.", "transp_no_match": "لا توجد وثيقة مطابقة لهذه التصفية.",
    "transp_commit_lead": "ما تلتزم المنصة بنشره ومراقبته:", "transp_more": "اطلعوا على القواعد في 10 نقاط",
    "desc_partenariat": "دعم التعليم الإسلامي المنظم في كوت ديفوار: دعم تقني ومالي ومؤسساتي وعيني.",
    "partner_title": "كونوا شركاء المنصة", "partner_lead": "هل ترغبون في دعم التعليم الإسلامي المنظم في كوت ديفوار؟ إليكم كيف نعمل معا.",
    "partner_why_title": "لماذا الشراكة مع المنصة",
    "partner_why": [
        {"i": "handshake", "t": "محاور واحد", "d": "نقطة دخول واحدة إلى المنظمات الوطنية للتعليم الإسلامي المنضوية في الاتحاد."},
        {"i": "shield", "t": "تسيير مراقب", "d": "مجلس إدارة ومفوضان للحسابات وتوقيع مزدوج لعمليات السحب وسجل للهبات."},
        {"i": "pin", "t": "حضور في كل البلاد", "d": "ممثلون جهويون لدى المديريات الجهوية للتربية الوطنية الإحدى والأربعين."},
    ],
    "partner_ways_title": "كيف تدعموننا",
    "partner_ways": [
        {"i": "book", "t": "دعم تقني", "d": "تكوين المعلمين وتوحيد البرامج وتنظيم الامتحانات وتسيير المدارس."},
        {"i": "scale", "t": "دعم مالي", "d": "المساهمة في برامج الاتحاد. تُسجل كل هبة في سجل الهبات: المتبرع والتاريخ والطبيعة والمبلغ."},
        {"i": "flag", "t": "دعم مؤسساتي", "d": "الربط مع الدولة وإدارات التربية، من أجل إدماج الهياكل الإسلامية للتعليم في المنظومة النظامية."},
        {"i": "users", "t": "دعم عيني", "d": "عتاد وتجهيزات أو خبرة توضع رهن إشارة المدارس والبرامج."},
    ],
    "partner_steps_title": "كيف يتم ذلك",
    "partner_steps": [
        {"t": "تواصلوا معنا", "d": "راسلونا على واتساب أو اتصلوا بالأمانة."},
        {"t": "نحدد الحاجة", "d": "نتبادل حول أهدافكم وحول المدارس أو البرامج المعنية."},
        {"t": "نضفي الطابع الرسمي على الدعم", "d": "يتفق على شكل الشراكة مع المسؤولين المعنيين في المنصة."},
    ],
    "partner_trust": "مساهماتكم مُتتبَّعة: سجل الهبات والتوقيع المزدوج لعمليات السحب والبيانات المالية المقدمة للأعضاء قبل الجمعية.",
    "partner_cta_call": "اتصلوا بالأمانة", "partner_cta_see": "اطلعوا على شركائنا", "partner_cta_transp": "زوروا مركز الشفافية",
    "desc_guide": "خطوة بخطوة: تسجيل الدخول ومتابعة الاشتراكات وتحميل الوصولات والشهادات والاطلاع على الجمعيات والتحقق من وثيقة.",
    "guide_title": "دليل فضاء الأعضاء", "guide_lead": "كل ما يمكن لمنظمتكم فعله عبر الإنترنت، خطوة بخطوة.",
    "guide_soon": "سيفتح الفضاء الإلكتروني قريبا: يهيئكم هذا الدليل لاستعماله.", "guide_login": "الدخول إلى فضاء الأعضاء",
    "guide_steps": [
        {"i": "users", "t": "تسجيل الدخول", "d": "تنشئ الأمانة حساب ممثل منظمتكم. سجلوا الدخول بالبريد الإلكتروني وكلمة المرور المسلّمين إليكم، ثم غيّروا كلمة المرور منذ أول دخول."},
        {"i": "file", "t": "الاطلاع على بطاقة المنظمة", "d": "بيانات الاتصال وولايات الممثلين ووضعية اشتراكاتكم."},
        {"i": "scale", "t": "متابعة الاشتراكات", "d": "يعرض كل استحقاق (الاشتراك السنوي، رسم الانخراط، الاشتراك الاستثنائي) المبلغ المستحق والمبلغ المدفوع والرصيد."},
        {"i": "check", "t": "تحميل الوصولات والشهادات", "d": "كل دفعة تعطي وصلا بصيغة PDF. وبعد تسوية الاشتراك السنوي، تحملون شهادة الاشتراك."},
        {"i": "book", "t": "الاطلاع على الجمعيات", "d": "الاستدعاءات بصيغة PDF وجدول الأعمال ومحاضر الجمعيات المستدعاة أو المنعقدة."},
        {"i": "qr", "t": "التحقق من وثيقة", "d": "امسحوا رمز QR الخاص بوصل أو شهادة أو شهادة انخراط: يؤكد الموقع أصالتها."},
    ],
    "guide_faq_title": "أسئلة شائعة",
    "guide_faq": [
        {"q": "من يمكنه تسجيل الدخول؟", "a": "الممثل الذي تعينه كل منظمة عضو، ومسؤولو هيئات المنصة حسب أدوارهم."},
        {"q": "نسيت كلمة المرور.", "a": "اتصلوا بالأمانة: يمكن لأحد المسؤولين مساعدتكم."},
        {"q": "هل ترى المنظمات الأخرى معلوماتي؟", "a": "لا. كل منظمة لا ترى إلا معلوماتها، وعمليات الدخول محمية."},
        {"q": "هل يمكن تتبع طلب الانخراط؟", "a": "نعم: يتيح رمز المتابعة المسلّم عند الإيداع الاطلاع على حالة الطلب دون حساب."},
    ],
    "guide_track": "تتبع طلب الانخراط", "guide_verify": "التحقق من وثيقة",
})
