from Preprocessing_Parsing import ResumeProcessor

class Job_Description:
    def jd_skill(self, jd):
        resume_processor = ResumeProcessor()
        resume_processor.load_skill_patterns("jz_skill_patterns.jsonl")
        jd_entities = resume_processor.extracting_entities(jd)
        jd_skills = jd_entities.get("SKILL", [])
        return jd_skills

    def find_not_in_resume(self, resume, jd):
        resume_processor = ResumeProcessor()
        resume_processor.load_skill_patterns("jz_skill_patterns.jsonl")
        
        # Extract Resume Skills
        resume_entities = resume_processor.extracting_entities(resume)
        resume_skills = resume_entities.get("SKILL", [])
        
        # Extracting Job Description Skills
        jd_entities = resume_processor.extracting_entities(jd)
        jd_skills = jd_entities.get("SKILL", [])
        
        return [skill for skill in jd_skills if skill not in resume_skills]
