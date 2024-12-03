import os
import google.generativeai as genai
import PyPDF2

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(job_descriptions, pdf_contents, prompt):
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    responses = model.generate_content([job_descriptions, pdf_contents, prompt])
    return responses.text


file_path = r"SaurabhGupta-AI-BRT 2.pdf"


def extract_text_from_pdf(file_):
    text = ""

    with open(file_, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
        return text


pdf_content = extract_text_from_pdf(file_path)


job_description = input("Enter your desired JOB DESCRIPTION:  \n")


prompt_1 = """
            You are skilled ATS (Application Tracking System) scanner and an experienced Technical HR with Tech Experience 
            in the field of any one job role from Data Science, Cyber Security, Full stack web development, Python developer, 
            Front end web developer, Java Spring developer, Big Data, Storage admin, NetAPP, Data Analyst, DEVOPS, Cloud,
            relationship manager, sales executive, dispute resolver,  marketing executive, business development associate, 
            sales associate, management trainee, sales trainee etc. 
            Your task is to review the provided resume against the job description for these profiles.
            Please share your professional evaluation on whether the candidate's profile aligns with the role.
            If it matches with the  job description, then give the strengths & weakness in the form of keywords only which can simplify my process.
            First the output comes as percentage and then keywords. If the profile doesn't match with the given job description 
            make the output as zero percentage and tell the profile doesn't match with given description.
           """

response = get_gemini_response(prompt_1, pdf_content, job_description)
print("The Response is : \n", response)
