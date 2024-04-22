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
  ItemLink TEXT NOT NULL,
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

CREATE TABLE UserTodoList(
  TaskID TEXT PRIMARY KEY,
  id TEXT NOT NULL,
  TaskName TEXT NOT NULL,
  FOREIGN KEY(id) REFERENCES user(id),
);

INSERT INTO Modules VALUES ('1', 'Resume Workshop', 'True');
INSERT INTO Modules VALUES ('2', 'LinkedIn and Social Media', 'True');
INSERT INTO Modules VALUES ('3', 'Interview Preparation', 'True');
INSERT INTO Modules VALUES ('4', 'Additional Advice', 'True');
INSERT INTO Modules VALUES ('5', 'Wrapping It All Up', 'True');

INSERT INTO ModuleItems VALUES ('1', 'The importance of a strong resume', 'https://edu.gcfglobal.org/en/resumewriting/why-you-need-a-resume/1/', 'True', '1');
INSERT INTO ModuleItems VALUES ('2', 'Common resume templates', 'https://www.myperfectresume.com/resume/formats', 'True', '1');
INSERT INTO ModuleItems VALUES ('3', 'What should you include on a resume?', 'https://www.indeed.com/career-advice/resumes-cover-letters/what-to-include-on-a-resume', 'True', '1');
INSERT INTO ModuleItems VALUES ('4', 'How to tailor your educational and work experience', 'https://www.topresume.com/career-advice/a-quick-guide-to-education-placement-on-your-resume', 'True', '1');
INSERT INTO ModuleItems VALUES ('5', 'Examples of professional resumes', 'https://careers.dasa.ncsu.edu/resumes/', 'True', '1');
INSERT INTO ModuleItems VALUES ('6', 'Create one yourself', 'https://www.indeed.com/create-resume', 'True', '1');

INSERT INTO ModuleItems VALUES ('7', 'What is LinkedIn?', 'https://www.techtarget.com/whatis/definition/LinkedIn', 'True', '2');
INSERT INTO ModuleItems VALUES ('8', 'Setting up a professional profile', 'https://blog.hubspot.com/marketing/linkedin-profile-perfection-cheat-sheet', 'True', '2');
INSERT INTO ModuleItems VALUES ('9', 'How does networking work on LinkedIn?', 'https://www.business.com/articles/linkedin-networking-tips/', 'True', '2');
INSERT INTO ModuleItems VALUES ('10', 'Examples of appealing LinkedIn profiles', 'https://www.inlytics.io/guide/linkedin-profile-examples', 'True', '2');

INSERT INTO ModuleItems VALUES ('11', 'What to expect from an interview', 'https://www.entrepreneur.com/living/heres-what-to-expect-in-a-job-interview-in-todays-job/457112', 'True', '3');
INSERT INTO ModuleItems VALUES ('12', 'Using the STAR structure to tailor your interview approach', 'https://www.themuse.com/advice/star-interview-method', 'True', '3');
INSERT INTO ModuleItems VALUES ('13', 'What do recruiters expect from you?', 'https://www.themuse.com/advice/star-interview-method', 'True', '3');
INSERT INTO ModuleItems VALUES ('14', 'Examples of mock interviews', 'https://www.youtube.com/watch?v=T1vTofBM_uA', 'True', '3');

INSERT INTO ModuleItems VALUES ('15', 'How to attain reference letters', 'https://www.coursera.org/articles/how-to-ask-for-a-letter-of-recommendation-template-tips', 'True', '4');
INSERT INTO ModuleItems VALUES ('16', 'Are cover letters important?', 'https://www.forbes.com/sites/ashleystahl/2023/06/12/everything-you-need-to-know-about-a-cover-letter-and-why-its-still-important/?sh=48ca5c455665', 'True', '4');
INSERT INTO ModuleItems VALUES ('17', 'Top skills employers want', 'https://www.prospects.ac.uk/careers-advice/applying-for-jobs/what-skills-do-employers-want', 'True', '4');

INSERT INTO ModuleItems VALUES ('18', 'What should I do now?', 'https://www.indeed.com/career-advice/finding-a-job/what-to-do-after-college', 'True', '5');
INSERT INTO ModuleItems VALUES ('19', 'Putting newfound skills to work', 'https://www.creditkarma.com/income/i/upskilling', 'True', '5');
INSERT INTO ModuleItems VALUES ('20', 'Expectations vs reality', 'https://sapienceanalytics.com/workforce-efficiency-expectations-vs-reality/', 'True', '5');
INSERT INTO ModuleItems VALUES ('21', 'Tips to keep in mind', 'https://www.vox.com/even-better/23719790/post-graduation-advice-life-work-money', 'True', '5');
INSERT INTO ModuleItems VALUES ('22', 'Advice from established professionals', 'https://www.linkedin.com/pulse/basic-advice-job-seeking-professionals-andrew-beach/', 'True', '5');
