CREATE TABLE user (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  major TEXT NULL,
  year TEXT NULL,
  gpa TEXT NULL,
  advisor TEXT NULL,
  Enrollment_Status TEXT NULL,
  level TEXT NULL,
  program TEXT NULL,
  college TEXT NULL
);