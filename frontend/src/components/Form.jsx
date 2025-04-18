import { useState, useEffect } from "react";
import axios from "axios";
import { API_BASE } from "../config/constants";
import LastSubmissionDisplay from "./LastSubmissionDisplay";

export default function SubmissionForm() {
  const INITIAL_STATE = { name: "", band: "", reason: "", year: "" };
  const [form, setForm] = useState(INITIAL_STATE);
  const [lastSubmission, setLastSubmission] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    axios.get(`${API_BASE}/submissions/last`)
      .then(res => setLastSubmission(res.data))
      .catch(() => setLastSubmission(null))
      .finally(() => setLoading(false));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    setError("");
  
    if (form.band.trim().length < 3) {
      setError("Please enter a real band name (at least 3 characters).");
      setSubmitting(false);
      return;
    }
  
    const payload = { ...form, year: parseInt(form.year) };
  
    try {
      const res = await axios.post(`${API_BASE}/submissions`, payload);
      setLastSubmission(res.data);
      setForm(INITIAL_STATE);
    } catch (err) {
      const message = err?.response?.data?.detail || "Something went wrong. Please try again.";
      setError(message);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto bg-white shadow-lg rounded-xl p-6">
      <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <input
          name="name"
          placeholder="Your name"
          required
          value={form.name}
          onChange={handleChange}
          className="border p-2 rounded"
        />

        <select
          name="year"
          required
          value={form.year}
          onChange={handleChange}
          className="border p-2 rounded"
        >
          <option value="">Select year</option>
          {Array.from({ length: 2025 - 1960 + 1 }, (_, i) => 1960 + i).map(y => (
            <option key={y} value={y}>{y}</option>
          ))}
        </select>

        <textarea
          name="band"
          placeholder="Favorite band"
          required
          value={form.band}
          onChange={handleChange}
          className="border p-2 rounded col-span-1 md:col-span-2"
        />

        <textarea
          name="reason"
          placeholder="Why you like them"
          required
          value={form.reason}
          onChange={handleChange}
          className="border p-2 rounded col-span-1 md:col-span-2"
        />

        <div className="col-span-1 md:col-span-2 text-right">
          <button
            type="submit"
            className="bg-purple-700 text-white px-4 py-2 rounded hover:bg-purple-800 disabled:opacity-50"
            disabled={submitting}
          >
            {submitting ? "Submitting..." : "Let's get rolling"}
          </button>
        </div>
      </form>

      {error && (
        <div className="bg-red-100 text-red-800 px-4 py-2 rounded mt-4">
          {error}
        </div>
      )}

      {!loading && <LastSubmissionDisplay submission={lastSubmission} />}
    </div>
  );
}