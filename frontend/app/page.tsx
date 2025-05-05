// frontend/app/page.tsx
import ChatUI from '../components/ChatUI';

export default function Home() {
  return (
    <main className="min-h-screen p-4">
      <h1 className="text-2xl font-bold mb-4">Groq Chatbot</h1>
      <ChatUI />
    </main>
  );
}
