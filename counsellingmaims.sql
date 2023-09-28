-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 28, 2023 at 08:57 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `counsellingmaims`
--

-- --------------------------------------------------------

--
-- Table structure for table `allowed_ip_addresses`
--

CREATE TABLE `allowed_ip_addresses` (
  `id` bigint(20) NOT NULL,
  `ip_address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `allowed_ip_addresses`
--

INSERT INTO `allowed_ip_addresses` (`id`, `ip_address`) VALUES
(1, '0.0.0.0');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

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
(25, 'Can add allowed ip', 7, 'add_allowedip'),
(26, 'Can change allowed ip', 7, 'change_allowedip'),
(27, 'Can delete allowed ip', 7, 'delete_allowedip'),
(28, 'Can view allowed ip', 7, 'view_allowedip'),
(29, 'Can add ballb', 8, 'add_ballb'),
(30, 'Can change ballb', 8, 'change_ballb'),
(31, 'Can delete ballb', 8, 'delete_ballb'),
(32, 'Can view ballb', 8, 'view_ballb'),
(33, 'Can add ballb temp', 9, 'add_ballbtemp'),
(34, 'Can change ballb temp', 9, 'change_ballbtemp'),
(35, 'Can delete ballb temp', 9, 'delete_ballbtemp'),
(36, 'Can view ballb temp', 9, 'view_ballbtemp'),
(37, 'Can add bank details', 10, 'add_bankdetails'),
(38, 'Can change bank details', 10, 'change_bankdetails'),
(39, 'Can delete bank details', 10, 'delete_bankdetails'),
(40, 'Can view bank details', 10, 'view_bankdetails'),
(41, 'Can add bba', 11, 'add_bba'),
(42, 'Can change bba', 11, 'change_bba'),
(43, 'Can delete bba', 11, 'delete_bba'),
(44, 'Can view bba', 11, 'view_bba'),
(45, 'Can add bballb', 12, 'add_bballb'),
(46, 'Can change bballb', 12, 'change_bballb'),
(47, 'Can delete bballb', 12, 'delete_bballb'),
(48, 'Can view bballb', 12, 'view_bballb'),
(49, 'Can add bballb temp', 13, 'add_bballbtemp'),
(50, 'Can change bballb temp', 13, 'change_bballbtemp'),
(51, 'Can delete bballb temp', 13, 'delete_bballbtemp'),
(52, 'Can view bballb temp', 13, 'view_bballbtemp'),
(53, 'Can add bba temp', 14, 'add_bbatemp'),
(54, 'Can change bba temp', 14, 'change_bbatemp'),
(55, 'Can delete bba temp', 14, 'delete_bbatemp'),
(56, 'Can view bba temp', 14, 'view_bbatemp'),
(57, 'Can add bcom', 15, 'add_bcom'),
(58, 'Can change bcom', 15, 'change_bcom'),
(59, 'Can delete bcom', 15, 'delete_bcom'),
(60, 'Can view bcom', 15, 'view_bcom'),
(61, 'Can add bcom temp', 16, 'add_bcomtemp'),
(62, 'Can change bcom temp', 16, 'change_bcomtemp'),
(63, 'Can delete bcom temp', 16, 'delete_bcomtemp'),
(64, 'Can view bcom temp', 16, 'view_bcomtemp'),
(65, 'Can add bjmc', 17, 'add_bjmc'),
(66, 'Can change bjmc', 17, 'change_bjmc'),
(67, 'Can delete bjmc', 17, 'delete_bjmc'),
(68, 'Can view bjmc', 17, 'view_bjmc'),
(69, 'Can add bjmc temp', 18, 'add_bjmctemp'),
(70, 'Can change bjmc temp', 18, 'change_bjmctemp'),
(71, 'Can delete bjmc temp', 18, 'delete_bjmctemp'),
(72, 'Can view bjmc temp', 18, 'view_bjmctemp'),
(73, 'Can add courses login', 19, 'add_courseslogin'),
(74, 'Can change courses login', 19, 'change_courseslogin'),
(75, 'Can delete courses login', 19, 'delete_courseslogin'),
(76, 'Can view courses login', 19, 'view_courseslogin'),
(77, 'Can add eco', 20, 'add_eco'),
(78, 'Can change eco', 20, 'change_eco'),
(79, 'Can delete eco', 20, 'delete_eco'),
(80, 'Can view eco', 20, 'view_eco'),
(81, 'Can add eco temp', 21, 'add_ecotemp'),
(82, 'Can change eco temp', 21, 'change_ecotemp'),
(83, 'Can delete eco temp', 21, 'delete_ecotemp'),
(84, 'Can view eco temp', 21, 'view_ecotemp'),
(85, 'Can add llm', 22, 'add_llm'),
(86, 'Can change llm', 22, 'change_llm'),
(87, 'Can delete llm', 22, 'delete_llm'),
(88, 'Can view llm', 22, 'view_llm'),
(89, 'Can add llm temp', 23, 'add_llmtemp'),
(90, 'Can change llm temp', 23, 'change_llmtemp'),
(91, 'Can delete llm temp', 23, 'delete_llmtemp'),
(92, 'Can view llm temp', 23, 'view_llmtemp'),
(93, 'Can add login', 24, 'add_login'),
(94, 'Can change login', 24, 'change_login'),
(95, 'Can delete login', 24, 'delete_login'),
(96, 'Can view login', 24, 'view_login');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$zK05Xna0lOZXOWeKaadbQ7$PwzUr4HBLgJUiGauanVSda4rBv56JBPcYQXpQQjlxCY=', '2023-09-28 17:43:09.973119', 1, 'chanm', '', '', 'chanmeetsinghsahni@gmail.com', 1, 1, '2023-09-28 17:19:17.982174');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ballb`
--

CREATE TABLE `ballb` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(255) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `ballb`
--

INSERT INTO `ballb` (`id`, `application_id`, `ipu_registration`, `allow_for_counselling`, `allow_editing`, `candidate_first_name`, `candidate_middle_name`, `candidate_last_name`, `dob`, `complete_address`, `email`, `candidate_number`, `gender`, `category`, `region`, `father_first_name`, `father_middle_name`, `father_last_name`, `mother_first_name`, `mother_middle_name`, `mother_last_name`, `father_qualification`, `mother_qualification`, `father_job`, `mother_job`, `father_job_designation`, `mother_job_designation`, `father_business_type`, `mother_business_type`, `father_number`, `mother_number`, `father_office_address`, `mother_office_address`, `guardian_name`, `board_12th`, `year_of_12th`, `rollno_12th`, `school_12th`, `aggregate_12th`, `first_subject_12th`, `second_subject_12th`, `third_subject_12th`, `fourth_subject_12th`, `other_subject_12th`, `other_subject_2_12th`, `board_10th`, `year_of_10th`, `rollno_10th`, `school_10th`, `aggregate_10th`, `maths_10th`, `science_10th`, `english_10th`, `sst_10th`, `other_subject_10th`, `other_subject_2_10th`, `cet_or_cuet`, `cet_rank`, `cet_rollno`, `special_achievements`, `passport_photo`, `cet_result`, `marksheet_10th`, `marksheet_12th`, `aadhaar`, `pancard`, `ipuregistrationproof`, `transaction_id`, `transaction_proof`, `counselling_transaction_id`, `counselling_transaction_proof`, `ip_address`, `forwarded_address`, `browser_info`, `created_at`) VALUES
(1, 'MAIMS/MQ/2023-24/26752992', 131230000001, 0, 0, 'CHANMEET', 'SINGH', 'SAHNI', '2023-09-28', 'CC 43 E HARI NAGAR', 'chanmeetsinghsahni@gmail.com', '8800675489', 'Male', 'UR/Gen', 'Delhi', 'HARVINDER', 'SINGH', 'SAHNI', 'HARPREET', 'KAUR', 'SAHNI', 'Intermediate', 'Graduate', 'Other', 'Teacher', 'EMPLOYEE', 'EMPLOYEE', '', '', '8826225210', '9968221340', '', '', '', 'CBSE', 2022, 2345234567, 'SSMS', 72.00, 87, 9, 90, 76, '98', '', 'CBSE', 2020, 2345234589, 'SSMS', 77.40, 77, 76, 79, 75, '80', '', 'CUET', 3400, '3456345612', 'NONE', 'ballb/photographs/131230000001.jpeg', 'ballb/cetresult/131230000001.pdf', 'ballb/marksheet10th/131230000001.pdf', 'ballb/marksheet12th/131230000001.pdf', 'ballb/aadhar/131230000001.pdf', 'ballb/pancard/131230000001.pdf', 'ballb/ipuregistration/131230000001.pdf', '12345', 'ballb/transactions/131230000001.pdf', '', '', '127.0.0.1', '-1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', '2023-09-28 22:54:22');

-- --------------------------------------------------------

--
-- Table structure for table `ballb_temp`
--

CREATE TABLE `ballb_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bank_details`
--

CREATE TABLE `bank_details` (
  `id` bigint(20) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `course` varchar(25) NOT NULL,
  `account_holder_name` varchar(75) NOT NULL,
  `account_number` varchar(50) NOT NULL,
  `bank_name` varchar(100) NOT NULL,
  `ifsc_code` varchar(50) NOT NULL,
  `cheque_copy` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bba`
--

CREATE TABLE `bba` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(255) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bballb`
--

CREATE TABLE `bballb` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(255) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `bballb`
--

INSERT INTO `bballb` (`id`, `application_id`, `ipu_registration`, `allow_for_counselling`, `allow_editing`, `candidate_first_name`, `candidate_middle_name`, `candidate_last_name`, `dob`, `complete_address`, `email`, `candidate_number`, `gender`, `category`, `region`, `father_first_name`, `father_middle_name`, `father_last_name`, `mother_first_name`, `mother_middle_name`, `mother_last_name`, `father_qualification`, `mother_qualification`, `father_job`, `mother_job`, `father_job_designation`, `mother_job_designation`, `father_business_type`, `mother_business_type`, `father_number`, `mother_number`, `father_office_address`, `mother_office_address`, `guardian_name`, `board_12th`, `year_of_12th`, `rollno_12th`, `school_12th`, `aggregate_12th`, `first_subject_12th`, `second_subject_12th`, `third_subject_12th`, `fourth_subject_12th`, `other_subject_12th`, `other_subject_2_12th`, `board_10th`, `year_of_10th`, `rollno_10th`, `school_10th`, `aggregate_10th`, `maths_10th`, `science_10th`, `english_10th`, `sst_10th`, `other_subject_10th`, `other_subject_2_10th`, `cet_or_cuet`, `cet_rank`, `cet_rollno`, `special_achievements`, `passport_photo`, `cet_result`, `marksheet_10th`, `marksheet_12th`, `aadhaar`, `pancard`, `ipuregistrationproof`, `transaction_id`, `transaction_proof`, `counselling_transaction_id`, `counselling_transaction_proof`, `ip_address`, `forwarded_address`, `browser_info`, `created_at`) VALUES
(1, 'MAIMS/MQ/2023-24/26752992', 131230000001, 0, 0, 'CHANMEET', 'SINGH', 'SAHNI', '2023-09-28', 'CC 43 E HARI NAGAR', 'chanmeetsinghsahni@gmail.com', '8800675489', 'Male', 'ST', 'Delhi', 'HARVINDER', 'SINGH', 'SAHNI', 'HARPREET', 'KAUR', 'SAHNI', 'Graduate', 'Post Graduate', 'Artist', 'Doctor', '', '', '', '', '8826225210', '9968221340', '', '', '', 'CBSE', 2022, 2345234567, 'SSMS', 65.50, 87, 9, 90, 76, '', '', 'CBSE', 2020, 2345234589, 'SSMS', 76.75, 77, 76, 79, 75, '', '', 'CET', 3400, '3456345612', '', 'bballb/photographs/131230000001.jpeg', 'bballb/cetresult/131230000001.pdf', 'bballb/marksheet10th/131230000001.pdf', 'bballb/marksheet12th/131230000001.pdf', 'bballb/aadhar/131230000001.pdf', 'bballb/pancard/131230000001.pdf', 'bballb/ipuregistration/131230000001.pdf', '12345', 'bballb/transactions/131230000001.pdf', '', '', '127.0.0.1', '-1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', '2023-09-28 22:57:16');

-- --------------------------------------------------------

--
-- Table structure for table `bballb_temp`
--

CREATE TABLE `bballb_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bba_temp`
--

CREATE TABLE `bba_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bcom`
--

CREATE TABLE `bcom` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(255) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bcom_temp`
--

CREATE TABLE `bcom_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bjmc`
--

CREATE TABLE `bjmc` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(255) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `bjmc_temp`
--

CREATE TABLE `bjmc_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `course_login`
--

CREATE TABLE `course_login` (
  `id` bigint(20) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `course` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `course_login`
--

INSERT INTO `course_login` (`id`, `ipu_registration`, `course`) VALUES
(1, 131230000001, 'BALLB'),
(2, 131230000001, 'BBALLB');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-09-28 17:21:07.546680', '1', '0.0.0.0', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-09-28 17:30:56.885618', '1', 'CHANMEET SAHNI', 2, '[{\"changed\": {\"fields\": [\"Allow editing\"]}}]', 12, 1),
(3, '2023-09-28 17:31:55.648574', '1', 'CHANMEET SAHNI', 2, '[{\"changed\": {\"fields\": [\"Allow for counselling\"]}}]', 12, 1),
(4, '2023-09-28 17:43:48.518878', '1', 'CHANMEET SAHNI', 2, '[{\"changed\": {\"fields\": [\"Allow for counselling\", \"Allow editing\"]}}]', 12, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'form', 'allowedip'),
(8, 'form', 'ballb'),
(9, 'form', 'ballbtemp'),
(10, 'form', 'bankdetails'),
(11, 'form', 'bba'),
(12, 'form', 'bballb'),
(13, 'form', 'bballbtemp'),
(14, 'form', 'bbatemp'),
(15, 'form', 'bcom'),
(16, 'form', 'bcomtemp'),
(17, 'form', 'bjmc'),
(18, 'form', 'bjmctemp'),
(19, 'form', 'courseslogin'),
(20, 'form', 'eco'),
(21, 'form', 'ecotemp'),
(22, 'form', 'llm'),
(23, 'form', 'llmtemp'),
(24, 'form', 'login'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-09-28 17:17:52.834559'),
(2, 'auth', '0001_initial', '2023-09-28 17:17:53.662472'),
(3, 'admin', '0001_initial', '2023-09-28 17:17:53.850875'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-09-28 17:17:53.866503'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-09-28 17:17:53.866503'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-09-28 17:17:54.017487'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-09-28 17:17:54.097266'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-09-28 17:17:54.121678'),
(9, 'auth', '0004_alter_user_username_opts', '2023-09-28 17:17:54.155863'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-09-28 17:17:54.214791'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-09-28 17:17:54.221487'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-09-28 17:17:54.230351'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-09-28 17:17:54.248527'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-09-28 17:17:54.272438'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-09-28 17:17:54.285559'),
(16, 'auth', '0011_update_proxy_permissions', '2023-09-28 17:17:54.305005'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-09-28 17:17:54.321459'),
(18, 'form', '0001_initial', '2023-09-28 17:17:54.821896'),
(19, 'sessions', '0001_initial', '2023-09-28 17:17:54.886581');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('qr01sobxrpemw96godacclguodtc0gu5', '.eJxVjMsOwiAQRf-FtSHC8HTpvt9ABgakaiAp7cr479qkC93ec859sYDbWsM28hJmYhcm2Ol3i5geue2A7thunafe1mWOfFf4QQefOuXn9XD_DiqO-q2jUuBAJZmMLckq46Qm4zyKaAFVNihKAW0pgXQekJxxNkMmEt4WfWbvD9AlN5A:1qlv2c:jlLxfU9bK8AePT2KohAWL3YTKgQu23SWyWZ2B3_3bcQ', '2023-10-12 17:43:10.000438');

-- --------------------------------------------------------

--
-- Table structure for table `eco`
--

CREATE TABLE `eco` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(255) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `eco_temp`
--

CREATE TABLE `eco_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `cet_or_cuet` varchar(10) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(100) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `llm`
--

CREATE TABLE `llm` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `allow_for_counselling` tinyint(1) NOT NULL,
  `allow_editing` tinyint(1) NOT NULL,
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED NOT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) NOT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED NOT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED NOT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) NOT NULL,
  `maths_10th` int(10) UNSIGNED NOT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED NOT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED NOT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED NOT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `ug_type` varchar(10) NOT NULL,
  `board_ug` varchar(75) NOT NULL,
  `year_of_ug` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_ug` >= 0),
  `rollno_ug` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_ug` >= 0),
  `school_ug` varchar(125) NOT NULL,
  `aggregate_ug` varchar(125) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(20) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `ug_degree` varchar(100) NOT NULL,
  `graduation_result` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `llm_temp`
--

CREATE TABLE `llm_temp` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `candidate_first_name` varchar(100) NOT NULL,
  `candidate_middle_name` varchar(100) NOT NULL,
  `candidate_last_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `complete_address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `candidate_number` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `father_first_name` varchar(100) NOT NULL,
  `father_middle_name` varchar(100) NOT NULL,
  `father_last_name` varchar(100) NOT NULL,
  `mother_first_name` varchar(100) NOT NULL,
  `mother_middle_name` varchar(100) NOT NULL,
  `mother_last_name` varchar(100) NOT NULL,
  `father_qualification` varchar(100) NOT NULL,
  `mother_qualification` varchar(100) NOT NULL,
  `father_job` varchar(100) NOT NULL,
  `mother_job` varchar(100) NOT NULL,
  `father_job_designation` varchar(100) NOT NULL,
  `mother_job_designation` varchar(100) NOT NULL,
  `father_business_type` varchar(100) NOT NULL,
  `mother_business_type` varchar(100) NOT NULL,
  `father_number` varchar(100) NOT NULL,
  `mother_number` varchar(100) NOT NULL,
  `father_office_address` varchar(100) NOT NULL,
  `mother_office_address` varchar(100) NOT NULL,
  `guardian_name` varchar(75) NOT NULL,
  `board_12th` varchar(255) NOT NULL,
  `year_of_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_12th` >= 0),
  `rollno_12th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_12th` >= 0),
  `school_12th` varchar(255) NOT NULL,
  `aggregate_12th` decimal(5,2) DEFAULT NULL,
  `first_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`first_subject_12th` >= 0),
  `second_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`second_subject_12th` >= 0),
  `third_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`third_subject_12th` >= 0),
  `fourth_subject_12th` int(10) UNSIGNED DEFAULT NULL CHECK (`fourth_subject_12th` >= 0),
  `other_subject_12th` varchar(10) NOT NULL,
  `other_subject_2_12th` varchar(10) NOT NULL,
  `board_10th` varchar(255) NOT NULL,
  `year_of_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_10th` >= 0),
  `rollno_10th` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_10th` >= 0),
  `school_10th` varchar(255) NOT NULL,
  `aggregate_10th` decimal(5,2) DEFAULT NULL,
  `maths_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`maths_10th` >= 0),
  `science_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`science_10th` >= 0),
  `english_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`english_10th` >= 0),
  `sst_10th` int(10) UNSIGNED DEFAULT NULL CHECK (`sst_10th` >= 0),
  `other_subject_10th` varchar(100) NOT NULL,
  `other_subject_2_10th` varchar(100) NOT NULL,
  `ug_type` varchar(10) NOT NULL,
  `board_ug` varchar(75) NOT NULL,
  `year_of_ug` int(10) UNSIGNED DEFAULT NULL CHECK (`year_of_ug` >= 0),
  `rollno_ug` bigint(20) UNSIGNED DEFAULT NULL CHECK (`rollno_ug` >= 0),
  `school_ug` varchar(125) NOT NULL,
  `aggregate_ug` varchar(125) NOT NULL,
  `cet_rank` int(10) UNSIGNED DEFAULT NULL CHECK (`cet_rank` >= 0),
  `cet_rollno` varchar(20) NOT NULL,
  `special_achievements` varchar(255) NOT NULL,
  `passport_photo` varchar(100) NOT NULL,
  `cet_result` varchar(100) NOT NULL,
  `marksheet_10th` varchar(100) NOT NULL,
  `marksheet_12th` varchar(100) NOT NULL,
  `aadhaar` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `ipuregistrationproof` varchar(100) NOT NULL,
  `ug_degree` varchar(100) NOT NULL,
  `graduation_result` varchar(100) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `transaction_proof` varchar(100) NOT NULL,
  `counselling_transaction_id` varchar(255) NOT NULL,
  `counselling_transaction_proof` varchar(100) NOT NULL,
  `ip_address` varchar(100) DEFAULT NULL,
  `forwarded_address` varchar(255) DEFAULT NULL,
  `browser_info` varchar(1000) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` bigint(20) NOT NULL,
  `application_id` varchar(100) NOT NULL,
  `ipu_registration` bigint(20) UNSIGNED NOT NULL CHECK (`ipu_registration` >= 0),
  `password` varchar(25) NOT NULL,
  `candidate_name` varchar(100) NOT NULL,
  `candidate_email` varchar(100) NOT NULL,
  `candidate_mobile` bigint(20) UNSIGNED NOT NULL CHECK (`candidate_mobile` >= 0),
  `ip_address` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `application_id`, `ipu_registration`, `password`, `candidate_name`, `candidate_email`, `candidate_mobile`, `ip_address`, `created_at`) VALUES
(1, 'MAIMS/MQ/2023-24/26752992', 131230000001, 'RWn0AFth0R4q', 'CHANMEET S', 'chanmeetsinghsahni@gmail.com', 8800675489, '127.0.0.1', '2023-09-28 17:21:46.264618');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `allowed_ip_addresses`
--
ALTER TABLE `allowed_ip_addresses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `ballb`
--
ALTER TABLE `ballb`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `ballb_temp`
--
ALTER TABLE `ballb_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bank_details`
--
ALTER TABLE `bank_details`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bba`
--
ALTER TABLE `bba`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bballb`
--
ALTER TABLE `bballb`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bballb_temp`
--
ALTER TABLE `bballb_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bba_temp`
--
ALTER TABLE `bba_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bcom`
--
ALTER TABLE `bcom`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bcom_temp`
--
ALTER TABLE `bcom_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bjmc`
--
ALTER TABLE `bjmc`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `bjmc_temp`
--
ALTER TABLE `bjmc_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `course_login`
--
ALTER TABLE `course_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `eco`
--
ALTER TABLE `eco`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `eco_temp`
--
ALTER TABLE `eco_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `llm`
--
ALTER TABLE `llm`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `llm_temp`
--
ALTER TABLE `llm_temp`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `application_id` (`application_id`),
  ADD UNIQUE KEY `ipu_registration` (`ipu_registration`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `allowed_ip_addresses`
--
ALTER TABLE `allowed_ip_addresses`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ballb`
--
ALTER TABLE `ballb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ballb_temp`
--
ALTER TABLE `ballb_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `bank_details`
--
ALTER TABLE `bank_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bba`
--
ALTER TABLE `bba`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bballb`
--
ALTER TABLE `bballb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `bballb_temp`
--
ALTER TABLE `bballb_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `bba_temp`
--
ALTER TABLE `bba_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bcom`
--
ALTER TABLE `bcom`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bcom_temp`
--
ALTER TABLE `bcom_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bjmc`
--
ALTER TABLE `bjmc`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bjmc_temp`
--
ALTER TABLE `bjmc_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `course_login`
--
ALTER TABLE `course_login`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `eco`
--
ALTER TABLE `eco`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `eco_temp`
--
ALTER TABLE `eco_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `llm`
--
ALTER TABLE `llm`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `llm_temp`
--
ALTER TABLE `llm_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
