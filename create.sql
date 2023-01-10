CREATE TABLE Courses
(
  course_id            INT   NOT NULL,
  course_title         char(100)  NOT NULL,
  organization_id      char(5)  NOT NULL,
  certification_id     char(4)  NOT NULL,
  difficulty_id        char(3)  NOT NULL,
  avg_rating           float8 NOT NULL,
  amount_of_students   float8 NOT NULL
);


CREATE TABLE Certifications
(
  certification_id      char(4)  NOT NULL,
  certification_name    char(20)  NOT NULL 
);


CREATE TABLE Organizations
(
  organization_id      char(5)  NOT NULL,
  organization_name    char(50)  NOT NULL
);


CREATE TABLE Difficulty
(
  difficulty_id       char(3)  NOT NULL,
  difficulty_level    char(40) NOT NULL  
);


ALTER TABLE Courses ADD PRIMARY KEY (course_id );
ALTER TABLE Certifications ADD PRIMARY KEY (certification_id);
ALTER TABLE Organizations ADD PRIMARY KEY (organization_id);
ALTER TABLE Difficulty ADD PRIMARY KEY (difficulty_id);

ALTER TABLE Courses ADD CONSTRAINT FK_Courses_Certifications FOREIGN KEY (certification_id) REFERENCES Certifications (certification_id);
ALTER TABLE Courses ADD CONSTRAINT FK_Courses_Organizations FOREIGN KEY (organization_id) REFERENCES Organizations (organization_id);
ALTER TABLE Courses ADD CONSTRAINT FK_Courses_Difficulty FOREIGN KEY (difficulty_id) REFERENCES Difficulty (difficulty_id);