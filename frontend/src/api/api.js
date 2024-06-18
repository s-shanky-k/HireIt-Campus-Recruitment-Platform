import axios from "axios";

export const baseURL = process.env.REACT_APP_API_BASE_URL;
export const student_login = "student/login";
export const recruiter_login = "recruiter/login";
export const all_job_postings = "student/job_openings";
export const student_apply_job = "student/apply";
export const student_applications = "student/applied";
export const student_search_by_name = "student/job_openings_by_name";
export const company_applicants = "company/view_applications";
export const decide_applicant_status = "company/decide";
export const get_stats = "/company/stats";
export const get_jobs_by_skills = "/student/jobs_by_skills";
export const get_student_by_skills = "/company/students_by_skills";
export const close_job = "/company/close";
export const create_job = "/company/create";
export const delete_job = "/company/delete";
export const job_postings = "/company/postings";

export const api = axios.create({
	baseURL: baseURL,
});

export const apiStudentLogin = async (credentials) => {
	try {
		const response = await api.post(
			`${student_login}`,
			{
				student_id: credentials.student_id,
				pwd: credentials.pwd,
			},
			{
				headers: {
					"Content-Type": "application/json",
				},
			}
		);
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiRecruiterLogin = async (credentials) => {
	try {
		const response = await api.post(`${recruiter_login}`, {
			recruiter_id: credentials.recruiter_id,
			pwd: credentials.pwd,
		});
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiStudentAllJobPostings = async (params) => {
	try {
		const response = await api.get(`${all_job_postings}`, {
			params: {
				student_id: params.student_id,
				count: params.count,
			},
		});
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiStudentApplyJob = async (params) => {
	// console.log("Params", params);
	try {
		const response = await api.post(`${student_apply_job}`, {
			student_id: params.student_id,
			job_id: params.job_id,
		});
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiStudentAllApplications = async (params) => {
	try {
		const response = await api.get(`${student_applications}`, {
			params: {
				student_id: params.student_id,
				count: params.count,
			},
		});
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiStudentFetchByName = async (params) => {
	try {
		const response = await api.get(`${student_search_by_name}`, {
			params: {
				student_id: params.student_id,
				company_name: params.company_name,
			},
		});
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiCompanyApplicants = async (params) => {
	try {
		const response = await api.get(`${company_applicants}`, {
			params: {
				company_id: params.company_id,
				count: params.count,
			},
		});
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiDecideApplicantStatus = async (params) => {
	try {
		const response = await api.put(`${decide_applicant_status}`, {
			job_id: params.job_id,
			student_id: params.student_id,
			status: params.status,
		});
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiGetStats = async (params) => {
	try {
		const response = await api.get(`${get_stats}/${params.company_id}`);
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiGetJobsBySkills = async (params) => {
	try {
		const response = await api.get(
			`${get_jobs_by_skills}/${params.student_id}`
		);
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiStudentsBySkills = async (params) => {
	try {
		const response = await api.get(
			`${get_student_by_skills}/${params.job_id}`
		);
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiCloseJobs = async (params) => {
	try {
		const response = await api.put(`${close_job}`, {
			job_id: params.job_id,
		});
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiCreateJob = async (params) => {
	try {
		const response = await api.post(`${create_job}`, {
			job_title: params.job_title,
			salary: params.salary,
			location: params.location,
			job_type: params.job_type,
			company_id: params.company_id,
			skill_names: params.skill_names,
		});
		// console.log(response);
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiDeleteJob = async (params) => {
	try {
		const response = await axios.delete(`${delete_job}/${params.job_id}`);
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};

export const apiGetJobPostings = async (params) => {
	try {
		const response = await api.get(`${job_postings}`, {
			params: {
				company_id: params.company_id,
				count: params.count,
			},
		});
		// console.log(response);
		return response.data;
	} catch (error) {
		return error.response.data;
	}
};
