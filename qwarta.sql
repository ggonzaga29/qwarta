SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add loan', 7, 'add_loan'),
(26, 'Can change loan', 7, 'change_loan'),
(27, 'Can delete loan', 7, 'delete_loan'),
(28, 'Can view loan', 7, 'view_loan'),
(29, 'Can add user', 8, 'add_user'),
(30, 'Can change user', 8, 'change_user'),
(31, 'Can delete user', 8, 'delete_user'),
(32, 'Can view user', 8, 'view_user'),
(33, 'Can add admin', 9, 'add_admin'),
(34, 'Can change admin', 9, 'change_admin'),
(35, 'Can delete admin', 9, 'delete_admin'),
(36, 'Can view admin', 9, 'view_admin'),
(37, 'Can add client', 10, 'add_client'),
(38, 'Can change client', 10, 'change_client'),
(39, 'Can delete client', 10, 'delete_client'),
(40, 'Can view client', 10, 'view_client'),
(41, 'Can add payment', 11, 'add_payment'),
(42, 'Can change payment', 11, 'change_payment'),
(43, 'Can delete payment', 11, 'delete_payment'),
(44, 'Can view payment', 11, 'view_payment'),
(45, 'Can add credit score', 12, 'add_creditscore'),
(46, 'Can change credit score', 12, 'change_creditscore'),
(47, 'Can delete credit score', 12, 'delete_creditscore'),
(48, 'Can view credit score', 12, 'view_creditscore');

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$hSwD3TuXov523Uvz3keDla$IZAD+djYbVsdkU/c4Igwqjl4pkhOu6YNnASvf4O1ke4=', '2023-07-26 17:15:40.327177', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2023-07-26 15:32:05.846978');

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `core_admin` (
  `user_ptr_id` int(11) NOT NULL,
  `salary` int(11) NOT NULL,
  `hire_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `core_admin` (`user_ptr_id`, `salary`, `hire_date`) VALUES
(1, 10000, '2023-07-26');

CREATE TABLE `core_client` (
  `user_ptr_id` int(11) NOT NULL,
  `occupation` varchar(50) NOT NULL,
  `monthly_income` decimal(10,2) NOT NULL,
  `net_worth` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `core_client` (`user_ptr_id`, `occupation`, `monthly_income`, `net_worth`) VALUES
(24, 'Sample Occupation', 2463.00, 44842.00),
(25, 'Sample Occupation', 2077.00, 19543.00),
(26, 'Sample Occupation', 2995.00, 33425.00),
(27, 'Sample Occupation', 2047.00, 25003.00),
(28, 'Sample Occupation', 3569.00, 38416.00),
(29, 'Sample Occupation', 1783.00, 11263.00),
(30, 'Sample Occupation', 2130.00, 25568.00),
(31, 'Sample Occupation', 1079.00, 16720.00),
(32, 'Sample Occupation', 1436.00, 43154.00),
(33, 'Sample Occupation', 2166.00, 22591.00),
(34, 'Sample Occupation', 3924.00, 30293.00),
(35, 'Sample Occupation', 2799.00, 18932.00),
(36, 'Sample Occupation', 1433.00, 40512.00),
(37, 'Sample Occupation', 3362.00, 12920.00),
(38, 'Sample Occupation', 2819.00, 44985.00);

CREATE TABLE `core_creditscore` (
  `credit_score_id` int(11) NOT NULL,
  `score` int(11) NOT NULL,
  `date_updated` date NOT NULL,
  `remarks` longtext NOT NULL,
  `client_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `core_creditscore` (`credit_score_id`, `score`, `date_updated`, `remarks`, `client_id_id`) VALUES
(18, 832, '2023-07-26', 'Sample Remarks', 24),
(19, 843, '2023-07-26', 'Sample Remarks', 25),
(20, 582, '2023-07-26', 'Sample Remarks', 26),
(21, 365, '2023-07-26', 'Sample Remarks', 27),
(22, 386, '2023-07-26', 'Sample Remarks', 28),
(23, 558, '2023-07-26', 'Sample Remarks', 29),
(24, 489, '2023-07-26', 'Sample Remarks', 30),
(25, 679, '2023-07-26', 'Sample Remarks', 31),
(26, 816, '2023-07-26', 'Sample Remarks', 32),
(27, 608, '2023-07-26', 'Sample Remarks', 33),
(28, 594, '2023-07-26', 'Sample Remarks', 34),
(29, 307, '2023-07-26', 'Sample Remarks', 35),
(30, 515, '2023-07-26', 'Sample Remarks', 36),
(31, 359, '2023-07-26', 'Sample Remarks', 37),
(32, 601, '2023-07-26', 'Sample Remarks', 38);

CREATE TABLE `core_loan` (
  `loan_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `amount` int(11) NOT NULL,
  `interest_rate` decimal(5,2) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `loan_length` int(11) NOT NULL,
  `issue_date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `approved_by_id` int(11) DEFAULT NULL,
  `client_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `core_loan` (`loan_id`, `product_name`, `amount`, `interest_rate`, `start_date`, `end_date`, `loan_length`, `issue_date`, `status`, `approved_by_id`, `client_id_id`) VALUES
(11, 'Loan for Sofia Acosta', 1716, 7.37, '2023-07-26', '2023-11-15', 0, '2023-07-26', 'Approved', NULL, 24),
(12, 'Loan for Jensen Reyes', 4966, 9.05, '2023-07-26', '2024-04-26', 0, '2023-07-26', 'Paid', NULL, 25),
(13, 'Loan for Audrey Baxter', 2634, 5.06, '2023-07-26', '2023-10-20', 0, '2023-07-26', 'Pending', NULL, 26),
(14, 'Loan for Tomas Fischer', 1953, 5.89, '2023-07-26', '2023-11-19', 0, '2023-07-26', 'Approved', NULL, 27),
(15, 'Loan for Maci Moody', 2291, 7.07, '2023-07-26', '2024-01-12', 0, '2023-07-26', 'Approved', NULL, 28),
(16, 'Loan for Ryland Avalos', 3564, 7.24, '2023-07-26', '2024-06-09', 0, '2023-07-26', 'Approved', NULL, 29),
(17, 'Loan for Paloma Enriquez', 1209, 5.81, '2023-07-26', '2024-05-09', 0, '2023-07-26', 'Pending', NULL, 30),
(18, 'Loan for Elisha Wilkins', 4998, 6.25, '2023-07-26', '2023-10-16', 0, '2023-07-26', 'Paid', NULL, 31),
(19, 'Loan for Amalia Patton', 1475, 3.66, '2023-07-26', '2024-07-07', 0, '2023-07-26', 'Pending', NULL, 32),
(20, 'Loan for Moises Briggs', 3902, 4.70, '2023-07-26', '2023-09-21', 0, '2023-07-26', 'Approved', NULL, 33);

CREATE TABLE `core_payment` (
  `payment_id` int(11) NOT NULL,
  `due_date` date NOT NULL,
  `amount` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `date_paid` date NOT NULL,
  `loan_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `core_payment` (`payment_id`, `due_date`, `amount`, `status`, `date_paid`, `loan_id_id`) VALUES
(31, '2023-07-26', 67940, 'Paid', '2023-07-26', 11),
(32, '2023-07-26', 97802, 'Paid', '2023-07-26', 11),
(33, '2023-07-26', 92060, 'Pending', '2023-07-26', 11),
(34, '2023-07-26', 78669, 'Pending', '2023-07-26', 12),
(35, '2023-07-26', 61948, 'Paid', '2023-07-26', 12),
(36, '2023-07-26', 71467, 'Paid', '2023-07-26', 12),
(37, '2023-07-26', 83213, 'Paid', '2023-07-26', 13),
(38, '2023-07-26', 56152, 'Pending', '2023-07-26', 13),
(39, '2023-07-26', 73794, 'Pending', '2023-07-26', 13),
(40, '2023-07-26', 99884, 'Paid', '2023-07-26', 14),
(41, '2023-07-26', 71988, 'Paid', '2023-07-26', 14),
(42, '2023-07-26', 77448, 'Pending', '2023-07-26', 14),
(43, '2023-07-26', 72760, 'Paid', '2023-07-26', 15),
(44, '2023-07-26', 96954, 'Pending', '2023-07-26', 15),
(45, '2023-07-26', 83737, 'Pending', '2023-07-26', 15),
(46, '2023-07-26', 87485, 'Pending', '2023-07-26', 16),
(47, '2023-07-26', 89839, 'Pending', '2023-07-26', 16),
(48, '2023-07-26', 64793, 'Paid', '2023-07-26', 16),
(49, '2023-07-26', 81508, 'Paid', '2023-07-26', 17),
(50, '2023-07-26', 90087, 'Pending', '2023-07-26', 17),
(51, '2023-07-26', 54769, 'Pending', '2023-07-26', 17),
(52, '2023-07-26', 97403, 'Paid', '2023-07-26', 18),
(53, '2023-07-26', 58227, 'Paid', '2023-07-26', 18),
(54, '2023-07-26', 72981, 'Pending', '2023-07-26', 18),
(55, '2023-07-26', 70278, 'Paid', '2023-07-26', 19),
(56, '2023-07-26', 62612, 'Pending', '2023-07-26', 19),
(57, '2023-07-26', 72397, 'Paid', '2023-07-26', 19),
(58, '2023-07-26', 98672, 'Pending', '2023-07-26', 20),
(59, '2023-07-26', 61627, 'Paid', '2023-07-26', 20),
(60, '2023-07-26', 62362, 'Pending', '2023-07-26', 20);

CREATE TABLE `core_user` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile_number` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `core_user` (`user_id`, `username`, `password`, `email`, `first_name`, `last_name`, `address`, `mobile_number`) VALUES
(1, 'gian_gonzaga', 'root', 'gian@gmail.com', 'Gian', 'Gonzaga', 'Labangon, Cebu City', '09667334990'),
(24, 'sofiaacosta', 'sample_password', 'sofia.acosta@example.com', 'Sofia', 'Acosta', 'Sample Address', '1234567890'),
(25, 'jensenreyes', 'sample_password', 'jensen.reyes@example.com', 'Jensen', 'Reyes', 'Sample Address', '1234567890'),
(26, 'audreybaxter', 'sample_password', 'audrey.baxter@example.com', 'Audrey', 'Baxter', 'Sample Address', '1234567890'),
(27, 'tomasfischer', 'sample_password', 'tomas.fischer@example.com', 'Tomas', 'Fischer', 'Sample Address', '1234567890'),
(28, 'macimoody', 'sample_password', 'maci.moody@example.com', 'Maci', 'Moody', 'Sample Address', '1234567890'),
(29, 'rylandavalos', 'sample_password', 'ryland.avalos@example.com', 'Ryland', 'Avalos', 'Sample Address', '1234567890'),
(30, 'palomaenriquez', 'sample_password', 'paloma.enriquez@example.com', 'Paloma', 'Enriquez', 'Sample Address', '1234567890'),
(31, 'elishawilkins', 'sample_password', 'elisha.wilkins@example.com', 'Elisha', 'Wilkins', 'Sample Address', '1234567890'),
(32, 'amaliapatton', 'sample_password', 'amalia.patton@example.com', 'Amalia', 'Patton', 'Sample Address', '1234567890'),
(33, 'moisesbriggs', 'sample_password', 'moises.briggs@example.com', 'Moises', 'Briggs', 'Sample Address', '1234567890'),
(34, 'aliafaulkner', 'sample_password', 'alia.faulkner@example.com', 'Alia', 'Faulkner', 'Sample Address', '1234567890'),
(35, 'jabarilu', 'sample_password', 'jabari.lu@example.com', 'Jabari', 'Lu', 'Sample Address', '1234567890'),
(36, 'emanikirk', 'sample_password', 'emani.kirk@example.com', 'Emani', 'Kirk', 'Sample Address', '1234567890'),
(37, 'alessandronash', 'sample_password', 'alessandro.nash@example.com', 'Alessandro', 'Nash', 'Sample Address', '1234567890'),
(38, 'novahcameron', 'sample_password', 'novah.cameron@example.com', 'Novah', 'Cameron', 'Sample Address', '1234567890');

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-07-26 15:33:06.358877', '1', 'Admin object (1)', 1, '[{\"added\": {}}]', 9, 1),
(2, '2023-07-26 15:33:35.170645', '1', 'User object (1)', 2, '[{\"changed\": {\"fields\": [\"First name\"]}}]', 8, 1),
(3, '2023-07-26 17:13:39.553469', '18', 'Client object (18)', 3, '', 10, 1),
(4, '2023-07-26 17:13:39.554469', '17', 'Client object (17)', 3, '', 10, 1),
(5, '2023-07-26 17:13:39.555468', '16', 'Client object (16)', 3, '', 10, 1),
(6, '2023-07-26 17:13:39.557469', '15', 'Client object (15)', 3, '', 10, 1),
(7, '2023-07-26 17:13:39.558478', '14', 'Client object (14)', 3, '', 10, 1),
(8, '2023-07-26 17:13:39.559483', '13', 'Client object (13)', 3, '', 10, 1),
(9, '2023-07-26 17:13:39.559483', '12', 'Client object (12)', 3, '', 10, 1),
(10, '2023-07-26 17:13:39.560484', '11', 'Client object (11)', 3, '', 10, 1),
(11, '2023-07-26 17:13:39.561483', '10', 'Client object (10)', 3, '', 10, 1),
(12, '2023-07-26 17:13:39.562483', '9', 'Client object (9)', 3, '', 10, 1),
(13, '2023-07-26 17:13:39.563483', '8', 'Client object (8)', 3, '', 10, 1),
(14, '2023-07-26 17:13:39.564483', '7', 'Client object (7)', 3, '', 10, 1),
(15, '2023-07-26 17:13:39.564483', '6', 'Client object (6)', 3, '', 10, 1),
(16, '2023-07-26 17:13:39.565484', '5', 'Client object (5)', 3, '', 10, 1),
(17, '2023-07-26 17:13:39.566483', '4', 'Client object (4)', 3, '', 10, 1),
(18, '2023-07-26 17:13:39.567483', '3', 'Client object (3)', 3, '', 10, 1),
(19, '2023-07-26 17:13:39.568492', '2', 'Client object (2)', 3, '', 10, 1),
(20, '2023-07-26 17:14:01.568164', '23', 'Admin object (23)', 3, '', 9, 1),
(21, '2023-07-26 17:14:01.569171', '22', 'Admin object (22)', 3, '', 9, 1),
(22, '2023-07-26 17:14:01.570169', '21', 'Admin object (21)', 3, '', 9, 1),
(23, '2023-07-26 17:14:01.571171', '20', 'Admin object (20)', 3, '', 9, 1),
(24, '2023-07-26 17:14:01.572171', '19', 'Admin object (19)', 3, '', 9, 1);

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'core', 'admin'),
(10, 'core', 'client'),
(12, 'core', 'creditscore'),
(7, 'core', 'loan'),
(11, 'core', 'payment'),
(8, 'core', 'user'),
(6, 'sessions', 'session');

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-26 15:30:48.883885'),
(2, 'auth', '0001_initial', '2023-07-26 15:30:49.130806'),
(3, 'admin', '0001_initial', '2023-07-26 15:30:49.189567'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-07-26 15:30:49.194070'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-26 15:30:49.199076'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-07-26 15:30:49.241210'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-07-26 15:30:49.270044'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-07-26 15:30:49.286102'),
(9, 'auth', '0004_alter_user_username_opts', '2023-07-26 15:30:49.290612'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-07-26 15:30:49.315264'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-07-26 15:30:49.317660'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-07-26 15:30:49.322176'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-07-26 15:30:49.338772'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-07-26 15:30:49.372373'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-07-26 15:30:49.389237'),
(16, 'auth', '0011_update_proxy_permissions', '2023-07-26 15:30:49.392754'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-07-26 15:30:49.408810'),
(18, 'core', '0001_initial', '2023-07-26 15:30:49.575919'),
(19, 'sessions', '0001_initial', '2023-07-26 15:30:49.594645'),
(20, 'core', '0002_alter_client_monthly_income_alter_client_net_worth', '2023-07-26 15:37:19.811696');

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

ALTER TABLE `core_admin`
  ADD PRIMARY KEY (`user_ptr_id`);

ALTER TABLE `core_client`
  ADD PRIMARY KEY (`user_ptr_id`);

ALTER TABLE `core_creditscore`
  ADD PRIMARY KEY (`credit_score_id`),
  ADD KEY `core_creditscore_client_id_id_cf7b5065_fk_core_clie` (`client_id_id`);

ALTER TABLE `core_loan`
  ADD PRIMARY KEY (`loan_id`),
  ADD KEY `core_loan_approved_by_id_394be3ff_fk_core_admin_user_ptr_id` (`approved_by_id`),
  ADD KEY `core_loan_client_id_id_86b0a8e3_fk_core_client_user_ptr_id` (`client_id_id`);

ALTER TABLE `core_payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `core_payment_loan_id_id_7bcc8e4f_fk_core_loan_loan_id` (`loan_id_id`);

ALTER TABLE `core_user`
  ADD PRIMARY KEY (`user_id`);

ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);


ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `core_creditscore`
  MODIFY `credit_score_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

ALTER TABLE `core_loan`
  MODIFY `loan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

ALTER TABLE `core_payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

ALTER TABLE `core_user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;


ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `core_admin`
  ADD CONSTRAINT `core_admin_user_ptr_id_b762f301_fk_core_user_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `core_user` (`user_id`);

ALTER TABLE `core_client`
  ADD CONSTRAINT `core_client_user_ptr_id_e5908bcf_fk_core_user_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `core_user` (`user_id`);

ALTER TABLE `core_creditscore`
  ADD CONSTRAINT `core_creditscore_client_id_id_cf7b5065_fk_core_clie` FOREIGN KEY (`client_id_id`) REFERENCES `core_client` (`user_ptr_id`);

ALTER TABLE `core_loan`
  ADD CONSTRAINT `core_loan_approved_by_id_394be3ff_fk_core_admin_user_ptr_id` FOREIGN KEY (`approved_by_id`) REFERENCES `core_admin` (`user_ptr_id`),
  ADD CONSTRAINT `core_loan_client_id_id_86b0a8e3_fk_core_client_user_ptr_id` FOREIGN KEY (`client_id_id`) REFERENCES `core_client` (`user_ptr_id`);

ALTER TABLE `core_payment`
  ADD CONSTRAINT `core_payment_loan_id_id_7bcc8e4f_fk_core_loan_loan_id` FOREIGN KEY (`loan_id_id`) REFERENCES `core_loan` (`loan_id`);

ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
