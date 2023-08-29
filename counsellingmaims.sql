-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 29, 2023 at 11:42 AM
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
(25, 'Can add login', 7, 'add_login'),
(26, 'Can change login', 7, 'change_login'),
(27, 'Can delete login', 7, 'delete_login'),
(28, 'Can view login', 7, 'view_login'),
(29, 'Can add courses login', 8, 'add_courseslogin'),
(30, 'Can change courses login', 8, 'change_courseslogin'),
(31, 'Can delete courses login', 8, 'delete_courseslogin'),
(32, 'Can view courses login', 8, 'view_courseslogin'),
(33, 'Can add allowed ip', 9, 'add_allowedip'),
(34, 'Can change allowed ip', 9, 'change_allowedip'),
(35, 'Can delete allowed ip', 9, 'delete_allowedip'),
(36, 'Can view allowed ip', 9, 'view_allowedip'),
(37, 'Can add bank details', 10, 'add_bankdetails'),
(38, 'Can change bank details', 10, 'change_bankdetails'),
(39, 'Can delete bank details', 10, 'delete_bankdetails'),
(40, 'Can view bank details', 10, 'view_bankdetails'),
(41, 'Can add bba temp', 11, 'add_bbatemp'),
(42, 'Can change bba temp', 11, 'change_bbatemp'),
(43, 'Can delete bba temp', 11, 'delete_bbatemp'),
(44, 'Can view bba temp', 11, 'view_bbatemp'),
(45, 'Can add bba', 12, 'add_bba'),
(46, 'Can change bba', 12, 'change_bba'),
(47, 'Can delete bba', 12, 'delete_bba'),
(48, 'Can view bba', 12, 'view_bba'),
(49, 'Can add bcom temp', 13, 'add_bcomtemp'),
(50, 'Can change bcom temp', 13, 'change_bcomtemp'),
(51, 'Can delete bcom temp', 13, 'delete_bcomtemp'),
(52, 'Can view bcom temp', 13, 'view_bcomtemp'),
(53, 'Can add bcom', 14, 'add_bcom'),
(54, 'Can change bcom', 14, 'change_bcom'),
(55, 'Can delete bcom', 14, 'delete_bcom'),
(56, 'Can view bcom', 14, 'view_bcom'),
(57, 'Can add bjmc temp', 15, 'add_bjmctemp'),
(58, 'Can change bjmc temp', 15, 'change_bjmctemp'),
(59, 'Can delete bjmc temp', 15, 'delete_bjmctemp'),
(60, 'Can view bjmc temp', 15, 'view_bjmctemp'),
(61, 'Can add bjmc', 16, 'add_bjmc'),
(62, 'Can change bjmc', 16, 'change_bjmc'),
(63, 'Can delete bjmc', 16, 'delete_bjmc'),
(64, 'Can view bjmc', 16, 'view_bjmc'),
(65, 'Can add ballb temp', 17, 'add_ballbtemp'),
(66, 'Can change ballb temp', 17, 'change_ballbtemp'),
(67, 'Can delete ballb temp', 17, 'delete_ballbtemp'),
(68, 'Can view ballb temp', 17, 'view_ballbtemp'),
(69, 'Can add ballb', 18, 'add_ballb'),
(70, 'Can change ballb', 18, 'change_ballb'),
(71, 'Can delete ballb', 18, 'delete_ballb'),
(72, 'Can view ballb', 18, 'view_ballb'),
(73, 'Can add bballb temp', 19, 'add_bballbtemp'),
(74, 'Can change bballb temp', 19, 'change_bballbtemp'),
(75, 'Can delete bballb temp', 19, 'delete_bballbtemp'),
(76, 'Can view bballb temp', 19, 'view_bballbtemp'),
(77, 'Can add bballb', 20, 'add_bballb'),
(78, 'Can change bballb', 20, 'change_bballb'),
(79, 'Can delete bballb', 20, 'delete_bballb'),
(80, 'Can view bballb', 20, 'view_bballb'),
(81, 'Can add eco temp', 21, 'add_ecotemp'),
(82, 'Can change eco temp', 21, 'change_ecotemp'),
(83, 'Can delete eco temp', 21, 'delete_ecotemp'),
(84, 'Can view eco temp', 21, 'view_ecotemp'),
(85, 'Can add eco', 22, 'add_eco'),
(86, 'Can change eco', 22, 'change_eco'),
(87, 'Can delete eco', 22, 'delete_eco'),
(88, 'Can view eco', 22, 'view_eco'),
(89, 'Can add llm temp', 23, 'add_llmtemp'),
(90, 'Can change llm temp', 23, 'change_llmtemp'),
(91, 'Can delete llm temp', 23, 'delete_llmtemp'),
(92, 'Can view llm temp', 23, 'view_llmtemp'),
(93, 'Can add llm', 24, 'add_llm'),
(94, 'Can change llm', 24, 'change_llm'),
(95, 'Can delete llm', 24, 'delete_llm'),
(96, 'Can view llm', 24, 'view_llm');

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
(9, 'form', 'allowedip'),
(18, 'form', 'ballb'),
(17, 'form', 'ballbtemp'),
(10, 'form', 'bankdetails'),
(12, 'form', 'bba'),
(20, 'form', 'bballb'),
(19, 'form', 'bballbtemp'),
(11, 'form', 'bbatemp'),
(14, 'form', 'bcom'),
(13, 'form', 'bcomtemp'),
(16, 'form', 'bjmc'),
(15, 'form', 'bjmctemp'),
(8, 'form', 'courseslogin'),
(22, 'form', 'eco'),
(21, 'form', 'ecotemp'),
(24, 'form', 'llm'),
(23, 'form', 'llmtemp'),
(7, 'form', 'login'),
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
(1, 'contenttypes', '0001_initial', '2023-08-29 09:15:58.055895'),
(2, 'auth', '0001_initial', '2023-08-29 09:15:59.649580'),
(3, 'admin', '0001_initial', '2023-08-29 09:16:00.155302'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-08-29 09:16:00.171055'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-08-29 09:16:00.184019'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-08-29 09:16:00.682006'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-08-29 09:16:00.931133'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-08-29 09:16:00.946861'),
(9, 'auth', '0004_alter_user_username_opts', '2023-08-29 09:16:00.974694'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-08-29 09:16:01.069845'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-08-29 09:16:01.075849'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-08-29 09:16:01.085004'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-08-29 09:16:01.105065'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-08-29 09:16:01.129320'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-08-29 09:16:01.159950'),
(16, 'auth', '0011_update_proxy_permissions', '2023-08-29 09:16:01.169984'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-08-29 09:16:01.189942'),
(18, 'form', '0001_initial', '2023-08-29 09:16:02.172824'),
(19, 'sessions', '0001_initial', '2023-08-29 09:16:02.311614');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ballb_temp`
--
ALTER TABLE `ballb_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bballb_temp`
--
ALTER TABLE `bballb_temp`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

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
