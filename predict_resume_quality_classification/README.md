This experiment data comes from a study that sought to understand the influence of race and gender on job application callback rates. The study monitored job postings in Boston and Chicago for several months during 2001 and 2002 and used this to build up a set of test cases. Over this time period, the researchers randomly generating resumes to go out to a job posting, such as years of experience and education details, to create a realistic-looking resume. They then randomly assigned a name to the resume that would communicate the applicant's gender and race. The first names chosen for the study were selected so that the names would predominantly be recognized as belonging to black or white individuals. For example, Lakisha was a name that their survey indicated would be interpreted as a black woman, while Greg was a name that would generally be interpreted to be associated with a white male.

1. job_ad_id	Unique ID associated with the advertisement.
2. job_city	City where the job was located.
3. job_industry	Industry of the job.
4. job_type	Type of role.
5. job_fed_contractor	Indicator for if the employer is a federal contractor.
6. job_equal_opp_employer	Indicator for if the employer is an Equal Opportunity Employer.
7. job_ownership	The type of company, e.g. a nonprofit or a private company.
8. job_req_any	Indicator for if any job requirements are listed. If so, the other job_req_* fields give more detail.
9. job_req_communication	Indicator for if communication skills are required.
10. job_req_education	Indicator for if some level of education is required.
11. job_req_min_experience	Amount of experience required.
12. job_req_computer	Indicator for if computer skills are required.
13. job_req_organization	Indicator for if organization skills are required.
14. job_req_school	Level of education required.
15. received_callback	Indicator for if there was a callback from the job posting for the person listed on this resume.
16. firstname	The first name used on the resume.
17. race	Inferred race associated with the first name on the resume.
18. gender	Inferred gender associated with the first name on the resume.
19. years_college	Years of college education listed on the resume.
20. college_degree	Indicator for if the resume listed a college degree.
21. honors	Indicator for if the resume listed that the candidate has been awarded some honors.
22. worked_during_school	Indicator for if the resume listed working while in school.
23. years_experience	Years of experience listed on the resume.
24. computer_skills	Indicator for if computer skills were listed on the resume. These skills were adapted for listings, though the skills were assigned independently of other details on the resume.
25. special_skills	Indicator for if any special skills were listed on the resume.
26. volunteer	Indicator for if volunteering was listed on the resume.
27. military	Indicator for if military experience was listed on the resume.
28. employment_holes	Indicator for if there were holes in the person's employment history.
29. has_email_address	Indicator for if the resume lists an email address.
30. resume_quality	Each resume was generally classified as either lower or higher quality.