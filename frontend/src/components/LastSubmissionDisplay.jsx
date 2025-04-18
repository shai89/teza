import React from "react";

export default function LastSubmissionDisplay({ submission }) {
  if (!submission) return null;

  return (
    <div className="mt-8 border-t pt-4 space-y-3">
      <h2 className="text-xl font-semibold text-gray-800">🎤 Last Submission</h2>

      {submission.text && (
        <>
          <h4 className="font-semibold text-gray-700">🎧 AI Description:</h4>
          <p className="text-sm text-gray-800 whitespace-pre-line">{submission.text}</p>
        </>
      )}

      {submission.image_url && (
        <div className="mt-4">
          <h4 className="font-semibold text-gray-700">🖼️ AI-Generated Image:</h4>
          <img
            src={submission.image_url}
            alt={`Generated for ${submission.band}`}
            className="w-full max-w-xs rounded shadow-md border"
          />
        </div>
      )}

      <div className="pt-2 text-sm text-gray-700 space-y-1">
        <p><strong>👤 Name:</strong> {submission.name}</p>
        <p><strong>🎸 Band:</strong> {submission.band}</p>
        <p><strong>💬 Reason:</strong> {submission.reason}</p>
        <p><strong>📅 Year:</strong> {submission.year}</p>
      </div>
    </div>
  );
}