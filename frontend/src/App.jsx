import SubmissionForm from './components/Form'

function App() {
  return (
    <div className="min-h-screen bg-gray-100 px-4 py-10">
      <h1 className="text-3xl font-bold text-center flex items-center justify-center gap-2 mb-6">
        <span>🎵</span> Favorite Band Form
      </h1>
      <SubmissionForm />
    </div>
  )
}

export default App
