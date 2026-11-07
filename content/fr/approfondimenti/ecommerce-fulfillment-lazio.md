---
title: "E-commerce fulfillment dans le Latium : flux, heure limite, retours et messagers"
description: "Commandes e-commerce d'un e-commerçant du Latium : de la réception à l'expédition, heures limites, retours, messagers et distances depuis Rome."
date: 2026-10-02
url: "/fr/analyses/ecommerce-fulfillment-latium/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Intérieur d'un centre de distribution avec des colis prêts à l'expédition, photo d'archives"
summary: "L'exécution des commandes e-commerce confiée à un prestataire pour compte d'autrui suit un flux standard : intégration des commandes, prélèvement, emballage, remise au messager et gestion des retours. Pour un e-commerçant du Latium, les variables décisives sont l'heure limite d'acceptation des commandes, l'heure d'enlèvement des messagers et la distance routière du bassin de Rome."
faq:
  - q: "Qu'est-ce que le cut-off dans l'e-commerce fulfillment ?"
    a: "C'est l'heure limite avant laquelle une commande reçue par l'entrepôt est expédiée le jour même. Il dépend de l'heure d'enlèvement du messager et du temps nécessaire au prélèvement et à l'emballage ; les commandes reçues après le cut-off partent le jour ouvré suivant."
  - q: "De combien de temps le consommateur dispose-t-il pour retourner un produit acheté en ligne ?"
    a: "Le Codice del Consumo italien (D.Lgs. 206/2005, art. 52) accorde au consommateur 14 jours pour exercer son droit de rétractation sans indiquer de motif, en règle générale à compter de la livraison du bien. Le vendeur rembourse dans les 14 jours suivant la rétractation et peut différer le remboursement jusqu'à la récupération des biens ou la preuve de leur expédition."
  - q: "Quelle distance sépare Latina Scalo de Rome pour les livraisons e-commerce ?"
    a: "Selon le calcul d'itinéraire OSRM pour véhicule léger, le site de Via della Dinamica se trouve à environ 70 km de l'EUR (environ 70 minutes), à environ 50 km de Pomezia (environ 50 minutes) et à environ 34 km d'Aprilia (environ 36 minutes). Pour les poids lourds, les temps sont plus longs."
  - q: "Quelle est la valeur de l'e-commerce de produits en Italie ?"
    a: "Selon l'Osservatorio eCommerce B2c Netcomm de l'École polytechnique de Milan, les achats en ligne de produits en Italie sont estimés en 2025 à environ 40,1 milliards d'euros, en hausse de 6 % par rapport à 2024, soit 11,2 % du total des achats de produits."
  - q: "Quelles données faut-il pour lancer un service de fulfillment ?"
    a: "Nombre d'articles (SKU), dimensions et poids, commandes moyennes et de pointe par jour, lignes par commande, taux de retour attendu, messagers utilisés, plateforme de vente et mode d'échange des commandes, exigences d'emballage et supports promotionnels."
---

L'exécution des commandes e-commerce (fulfillment) est le segment de la logistique pour compte d'autrui au profil opérationnel le plus fragmenté : beaucoup de petites commandes, une ou deux lignes par commande, expédition au colis unique, une part de retours supérieure à celle du commerce traditionnel. Selon l'Osservatorio eCommerce B2c Netcomm de l'École polytechnique de Milan, cité par l'AGI le 27 mai 2025, les achats en ligne de produits en Italie sont estimés en 2025 à environ 40,1 milliards d'euros, en hausse de 6 % par rapport à 2024, soit 11,2 % du total des achats de produits.

Pour un e-commerçant du Latium, le choix de l'entrepôt se joue sur quelques paramètres mesurables : l'heure limite des commandes, l'heure d'enlèvement des messagers, la gestion des retours et la distance routière jusqu'aux clients finaux et aux hubs des messagers.

## Le flux, de la commande à la livraison

Le cycle d'une commande e-commerce gérée par un prestataire pour compte d'autrui se compose de sept étapes :

1. **réception de la marchandise** du fournisseur ou du fabricant, avec contrôle quantitatif, enregistrement des articles (SKU) et mise en stock ;
2. **intégration des commandes** : les commandes de la plateforme de vente parviennent au WMS (logiciel de gestion d'entrepôt) du prestataire par connecteur, fichier ou interface informatique ;
3. **prélèvement (picking)**, en règle générale à la pièce, avec regroupement de plusieurs commandes dans une même tournée de prélèvement pour réduire les parcours ;
4. **contrôle et emballage (packing)**, avec choix du carton, calage, insertion des documents et des supports promotionnels ;
5. **étiquetage** avec la lettre de voiture du messager et génération du numéro de suivi ;
6. **remise au messager** lors de l'enlèvement programmé et transmission du suivi à la plateforme ;
7. **gestion des retours** : réception, contrôle, décision sur la destination du produit et mise à jour du stock.

Les opérations de prélèvement, d'emballage et d'étiquetage sont décrites sur la page du service de [manutention]({{< relref "/servizi/handling" >}}) ; les besoins propres au secteur sur la page [e-commerce]({{< relref "/settori/ecommerce" >}}).

## Le cut-off et l'heure d'enlèvement

Le **cut-off** est l'heure limite avant laquelle une commande reçue est expédiée le jour même. Il se calcule à rebours à partir de l'heure d'enlèvement du messager : si le messager passe à 17 heures et que l'entrepôt met en moyenne deux heures pour prélever, emballer et consolider les colis d'une vague de commandes, le cut-off ne peut être postérieur à 15 heures ; les jours de pointe, il faut l'avancer ou renforcer le personnel.

Trois éléments déplacent le cut-off :

- le **nombre d'enlèvements** quotidiens et l'heure du dernier enlèvement, convenus avec chaque messager ;
- la **productivité du prélèvement**, qui dépend de l'organisation des emplacements : les articles les plus vendus doivent être placés près de la zone d'emballage ;
- la **qualité des données** de poids et de dimensions, qui déterminent le carton et le tarif du messager sans mesures manuelles.

Le contrat de service doit indiquer le cut-off et l'indicateur qui le mesure, par exemple le pourcentage de commandes reçues avant l'heure limite et expédiées le jour même. Sur ce sujet, voir le guide du [contrat de logistique pour compte d'autrui et des KPI]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Les messagers et la géographie du Latium

L'e-commerçant peut utiliser ses propres contrats avec les messagers express ou ceux négociés par le prestataire logistique. Les messagers nationaux enlèvent à l'entrepôt et trient les colis dans leurs propres hubs ; pour les livraisons B2B régionales ou portant sur un petit nombre de colis lourds, le prestataire peut employer sa propre flotte.

Pour un entrepôt à Latina Scalo, les distances routières vers les principaux bassins de demande, calculées avec le moteur d'itinéraire OSRM pour véhicule léger dans des conditions de trafic normal, sont les suivantes :

| Destination | Distance routière | Temps estimé |
|---|---|---|
| Latina centre | environ 8 km | environ 13 minutes |
| Aprilia | environ 34 km | environ 36 minutes |
| Pomezia | environ 50 km | environ 50 minutes |
| Santa Palomba | environ 55 km | environ 57 minutes |
| Castel Romano | environ 57 km | environ 56 minutes |
| Rome EUR | environ 70 km | environ 70 minutes |
| Rome Ostiense | environ 74 km | environ 76 minutes |
| Fiumicino | environ 90 km | environ 86 minutes |

Pour les poids lourds et aux heures de pointe, les temps sont plus longs. L'axe principal vers Rome est la route nationale 148 Pontina, à deux chaussées séparées entre Rome et Borgo Piave ; sur le tronçon entre Pomezia et Latina nord, la limite de vitesse a été abaissée de 110 à 80 km/h. Les fiches des différentes zones figurent sur les pages [logistique à Rome]({{< relref "/logistica/roma" >}}), [sud de Rome]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) et [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Les retours

Le **droit de rétractation** du consommateur est régi par le Codice del Consumo italien (D.Lgs. 206/2005). L'art. 52 accorde 14 jours pour se rétracter sans motif, en règle générale à compter de la livraison du bien. L'art. 56 oblige le vendeur à rembourser dans les 14 jours suivant la rétractation, avec la faculté de différer le remboursement jusqu'à la réception des biens ou la preuve de leur expédition.

L'entrepôt doit donc traiter les retours dans des délais compatibles avec ces échéances :

- **réception et enregistrement** du retour avec le numéro de commande d'origine ;
- **contrôle** de l'état du produit et de l'emballage selon des critères convenus avec l'e-commerçant ;
- **destination** : remise en stock, remise en état, reconditionnement, vente en second choix ou élimination ;
- **communication** du résultat à la plateforme pour débloquer le remboursement.

Une zone dédiée aux retours, séparée du stock vendable, évite qu'une marchandise non contrôlée redevienne disponible pour les commandes.

## Pics saisonniers et capacité

L'e-commerce concentre les volumes sur quelques périodes de l'année, liées aux promotions et aux fêtes. Pour le prestataire, cela suppose de prévoir du personnel supplémentaire, des emplacements de réserve et des accords avec les messagers pour des enlèvements supplémentaires. Pour l'e-commerçant, cela suppose de communiquer à l'avance les prévisions de ventes et les calendriers promotionnels : un pic non annoncé est la cause la plus fréquente du non-respect du cut-off.

## Le site de Latina Scalo

Le Consorzio Logistico Latina Scalo, Via della Dinamica à Latina Scalo (LT), dispose de 19 000 mètres carrés couverts et d'un système WMS pour la gestion de l'entrepôt. Les services comprennent le stockage, le prélèvement, l'emballage, l'étiquetage et la palettisation, le transport routier avec flotte dédiée et la distribution du dernier kilomètre, ainsi que la gestion documentaire. Selon le Consorzio, l'activité est assurée 24 heures sur 24, 7 jours sur 7. Les modalités d'intégration avec chaque plateforme de vente doivent être vérifiées au stade du devis. Pour la distribution sur Rome, voir l'analyse consacrée au [dernier kilomètre vers le sud de Rome]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Sources

- AGI, dépêche économique du 27 mai 2025 sur les achats en ligne de produits en 2025, données Osservatorio eCommerce B2c Netcomm – Politecnico di Milano : [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), artt. 52 e 56 : [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Distances et temps : calcul d'itinéraire OSRM (Open Source Routing Machine) depuis le site de Via della Dinamica, véhicule léger, trafic normal ; élaboration du Consorzio.
- SS148 Pontina, chaussées et limites de vitesse : [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (données ANAS)
- Services et activité : déclarations du Consorzio Logistico Latina Scalo.
