
# SUJET – Vues et vues matérialisées (Plateforme de streaming musical)

## Contexte

Tu travailles pour une **plateforme de streaming musical**.
Les équipes Data souhaitent analyser :

* les **morceaux disponibles**,
* les **utilisateurs Premium français**,
* les **écoutes détaillées** (qui a écouté quoi, quand et combien de temps),
* les **statistiques d’écoute par artiste**,
* la **performance des artistes par pays**.

Les concepts étudiés portent sur :

* les **vues classiques**,
* les **vues matérialisées**,
* les requêtes avec **JOIN** et **agrégats**,
* la **réutilisation de vues** dans d’autres requêtes.

Tu dois mettre en place des vues adaptées à ces besoins.

---

## 0. Préparation : schéma et données

Exécute d’abord ce script pour préparer les tables :

```sql
DROP TABLE IF EXISTS listenings;
DROP TABLE IF EXISTS tracks;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS users;

-- =========================
-- TABLE : users
-- =========================
CREATE TABLE users (
    user_id       INTEGER PRIMARY KEY,
    username      TEXT        NOT NULL,
    country       TEXT        NOT NULL,
    subscription  TEXT        NOT NULL  -- 'Free' ou 'Premium'
);

INSERT INTO users (user_id, username, country, subscription) VALUES
    (1, 'alice',   'France',  'Free'),
    (2, 'bruno',   'France',  'Premium'),
    (3, 'carla',   'Belgique','Premium'),
    (4, 'david',   'Canada',  'Free'),
    (5, 'emma',    'France',  'Premium');

-- =========================
-- TABLE : artists
-- =========================
CREATE TABLE artists (
    artist_id  INTEGER PRIMARY KEY,
    name       TEXT        NOT NULL,
    country    TEXT        NOT NULL
);

INSERT INTO artists (artist_id, name, country) VALUES
    (1, 'Electro Pulse',   'France'),
    (2, 'Rocking Stones',  'USA'),
    (3, 'LoFi Dreams',     'Canada');

-- =========================
-- TABLE : tracks
-- =========================
CREATE TABLE tracks (
    track_id   INTEGER PRIMARY KEY,
    title      TEXT        NOT NULL,
    duration_s INTEGER     NOT NULL,
    artist_id  INTEGER     NOT NULL REFERENCES artists(artist_id)
);

INSERT INTO tracks (track_id, title, duration_s, artist_id) VALUES
    (1, 'Morning Energy',  210, 1),
    (2, 'Night Runner',    190, 1),
    (3, 'Stone Highway',   230, 2),
    (4, 'Chill Vibes',     300, 3),
    (5, 'Deep Focus',      280, 3);

-- =========================
-- TABLE : listenings
-- =========================
CREATE TABLE listenings (
    listening_id   INTEGER PRIMARY KEY,
    user_id        INTEGER NOT NULL REFERENCES users(user_id),
    track_id       INTEGER NOT NULL REFERENCES tracks(track_id),
    listened_at    TIMESTAMP NOT NULL,
    seconds_played INTEGER NOT NULL
);

INSERT INTO listenings (listening_id, user_id, track_id, listened_at, seconds_played) VALUES
    (1, 1, 1, TIMESTAMP '2025-01-10 09:00:00', 180),
    (2, 1, 4, TIMESTAMP '2025-01-10 09:30:00', 200),
    (3, 2, 1, TIMESTAMP '2025-01-11 10:00:00', 210),
    (4, 2, 2, TIMESTAMP '2025-01-11 10:30:00', 190),
    (5, 2, 3, TIMESTAMP '2025-01-11 11:00:00', 230),
    (6, 3, 4, TIMESTAMP '2025-01-12 08:45:00', 250),
    (7, 3, 5, TIMESTAMP '2025-01-12 09:15:00', 260),
    (8, 4, 3, TIMESTAMP '2025-01-13 14:00:00', 120),
    (9, 5, 1, TIMESTAMP '2025-01-14 18:00:00', 210),
    (10,5, 5, TIMESTAMP '2025-01-14 18:30:00', 200);
```

---

## 1. Catalogue public des morceaux

Le service Produit souhaite afficher une liste publique des morceaux, contenant :

* les informations du morceau,
* la durée,
* le nom de l’artiste associé.

Créer une vue adaptée à ce besoin, puis l’utiliser pour lister l’ensemble du catalogue de manière ordonnée.

---

CREATE OR REPLACE VIEW v_music_results AS
SELECT
    t.*,
    a.name AS artist_name
FROM tracks AS t
LEFT JOIN artists AS a
    ON a.artist_id = t.artist_id;

    -- Utilisation : lire les résultats comme si c'était une table "flattened"
SELECT *
FROM v_music_results


## 2. Utilisateurs Premium français

L’équipe marketing souhaite travailler spécifiquement sur les utilisateurs :

* ayant un abonnement Premium,
* résidant en France.

Créer une vue filtrée permettant d’identifier ces utilisateurs, puis l’utiliser pour obtenir une liste ordonnée.

---

CREATE OR REPLACE VIEW v_users_premium_france AS
SELECT
    u.*
FROM users AS u
WHERE u.subscription = 'Premium'
  AND u.country = 'France';

SELECT *
FROM v_users_premium_france

## 3. Historique détaillé des écoutes

L’équipe Data souhaite une vue qui rassemble toutes les informations utiles sur les écoutes :

* l’utilisateur (identifiant, nom, pays),
* le morceau (titre),
* l’artiste,
* la date/heure d’écoute,
* la durée réellement écoutée.

Créer cette vue consolidée en utilisant les relations entre les tables, puis l’interroger pour extraire uniquement les écoutes réalisées par des utilisateurs français.

---

CREATE OR REPLACE VIEW v_listening AS
SELECT
 	u.username AS user_name,
    u.country AS user_country,
	t.title AS track_title,
	a.name AS artist_name,
	l.listened_at
   
FROM listenings AS l
LEFT JOIN users AS u
    ON u.user_id = l.user_id
LEFT JOIN tracks AS t
    ON t.track_id = l.track_id
LEFT JOIN artists AS a
    ON a.artist_id = t.artist_id
WHERE u.country = 'France'

SELECT * FROM v_listening

## 4. Statistiques d’écoute par artiste

Pour optimiser l’analyse, cette statistique doit être construite à partir d’une **vue matérialisée** reposant sur les écoutes détaillées :

Pour chaque artiste, calculer :

* le nombre total d’écoutes,
* le nombre total de secondes écoutées,
* la durée moyenne écoutée par écoute.

Créer cette vue matérialisée, puis l’utiliser pour identifier les artistes les plus écoutés selon différents critères (par exemple ceux qui ont un nombre d’écoutes élevé, ou un volume total de lecture important).

---

CREATE MATERIALIZED VIEW mv_artist_most_listen AS
SELECT
    a.artist_id,
    a.name,
	
    COUNT(a.artist_id) AS total_listens,
    SUM(l.seconds_played) AS total_seconds_listened
    AVG(l.seconds_played) AS moyenne_listened_by_listen

FROM listenings AS l, artists AS a

GROUP BY  a.artist_id, a.name

SELECT * 
FROM mv_artist_most_listen


## 5. Analyse par pays d’artiste

À partir des statistiques d’écoute par artiste, analyser maintenant la performance :

* par pays d’artiste,
* en regroupant l’ensemble des artistes du même pays.

Produire une requête donnant, pour chaque pays :

* le volume total d’écoute cumulé,
* le nombre d’artistes concernés,

et ordonner ce classement.

---

## 6. Optimisation et index

Certaines colonnes de ces vues matérialisées seront utilisées très souvent dans des filtres et tris (par exemple le total de secondes ou la moyenne par écoute).

Identifier les colonnes les plus pertinentes à indexer, et proposer les index adaptés pour optimiser ces usages.