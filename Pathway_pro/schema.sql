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

CREATE TABLE Modules(
  ModuleID TEXT PRIMARY KEY,
  ModuleName TEXT NOT NULL,
  active TEXT NOT NULL
);

CREATE TABLE ModuleItems(
  ModuleItemID TEXT PRIMARY KEY,
  ItemName TEXT NOT NULL,
  active TEXT NOT NULL,
  ModuleID TEXT NOT NULL,
  FOREIGN KEY(ModuleID) REFERENCES Modules(ModuleID)
);

CREATE TABLE UserSelections(
  id TEXT NOT NULL,
  ModuleItemID TEXT NOT NULL,
  FOREIGN KEY(id) REFERENCES user(id),
  FOREIGN KEY(ModuleItemID) REFERENCES ModuleItems(ModuleItemID),
  PRIMARY KEY(id, ModuleItemID)
);

