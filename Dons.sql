-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : db
-- Généré le : ven. 28 juil. 2023 à 07:23
-- Version du serveur : 8.0.33
-- Version de PHP : 8.1.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `Dons`
--

-- --------------------------------------------------------

--
-- Structure de la table `donateurs`
--

CREATE TABLE `donateurs` (
  `id` int NOT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `adresse` varchar(50) DEFAULT NULL,
  `code_postal` varchar(5) DEFAULT NULL,
  `ville` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `somme_recoltee` decimal(15,2) DEFAULT NULL,
  `horodatage` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `latitude` decimal(10,6) DEFAULT NULL,
  `longitude` decimal(10,6) DEFAULT NULL
) ;

--
-- Déchargement des données de la table `donateurs`
--

INSERT INTO `donateurs` (`id`, `nom`, `prenom`, `adresse`, `code_postal`, `ville`, `email`, `somme_recoltee`, `horodatage`, `latitude`, `longitude`) VALUES
(17, 'Le Gall', 'Jean', '1 Rue de la Plage', '29217', 'Le Conquet', 'jean.legall@example.com', 50.50, '2023-07-27 18:58:06', 48.390528, -4.486009),
(18, 'Le Meur', 'Marie', '15 Rue du Port', '29810', 'Plouarzel', 'marie.lemeur@example.com', 75.25, '2023-07-27 18:58:06', 48.445118, -4.773274),
(19, 'Le Goff', 'Pierre', '25 Rue des Dunes', '29250', 'Saint-Pol-de-Léon', 'pierre.legoff@example.com', 100.00, '2023-07-27 18:58:06', 48.677021, -3.986151),
(20, 'Le Bris', 'Anna', '8 Rue du Phare', '29280', 'Plouzané', 'anna.lebris@example.com', 25.75, '2023-07-27 18:58:06', 48.383053, -4.616372),
(21, 'Le Berre', 'Paul', '10 Rue de la Côte', '29830', 'Ploudalmézeau', 'paul.leberre@example.com', 150.00, '2023-07-27 18:58:06', 48.522896, -4.607393),
(22, 'Le Moal', 'Emma', '5 Rue des Abers', '29260', 'Lesneven', 'emma.lemoal@example.com', 30.50, '2023-07-27 18:58:06', 48.563824, -4.333789),
(23, 'Cariou', 'Ewenn', '20 Rue des Goémoniers', '29290', 'Saint-Renan', 'lucas.cariou@example.com', 200.25, '2023-07-27 18:58:06', 48.625078, -4.573191),
(24, 'Le Gall', 'Léa', '12 Rue de Kerhuon', '29480', 'Le Relecq-Kerhuon', 'lea.legall@example.com', 80.00, '2023-07-27 18:58:06', 48.394979, -4.426682),
(25, 'Le Gac', 'Hugo', '30 Rue de Plouigneau', '29610', 'Plouigneau', 'hugo.legac@example.com', 120.75, '2023-07-27 18:58:06', 48.613206, -3.787142),
(26, 'Abgrall', 'Clara', '16 rue de Lyon', '29200', 'Brest', 'clara.abgrall@example.com', 55.00, '2023-07-27 18:58:06', 48.390528, -4.486009);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `donateurs`
--
ALTER TABLE `donateurs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `donateurs`
--
ALTER TABLE `donateurs`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
