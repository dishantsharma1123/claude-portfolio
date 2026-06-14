"use client";
import React, { useState, useRef, useEffect } from 'react';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export default function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      // Removed Clerk token logic. Making a direct anonymous call.
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: input, history: messages }),
      });

      if (!response.body) throw new Error("No readable stream body context.");
      
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let assistantMessage: Message = { role: 'assistant', content: '' };
      
      setMessages((prev) => [...prev, assistantMessage]);

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        
        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            assistantMessage.content += data;
            setMessages((prev) => [...prev.slice(0, -1), { ...assistantMessage }]);
          }
        }
      }
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex-1 flex flex-col max-w-3xl mx-auto w-full px-4 h-full pt-8">
      <div className="flex-1 overflow-y-auto space-y-6 pr-2 pb-24">
        {messages.length === 0 && (
          <div className="text-center pt-24 space-y-4">
            <h1 className="text-3xl font-serif text-[#191919]">How can I help you navigate Dishant's career?</h1>
            <p className="text-sm text-gray-500">Ask about Elasticsearch optimizations, architecture, or 50M+ record systems.</p>
          </div>
        )}
        {messages.map((msg, idx) => (
          <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-2xl px-4 py-3 rounded-xl leading-relaxed text-sm ${msg.role === 'user' ? 'bg-[#f0ede4] text-gray-900 font-medium' : 'text-gray-800'}`}>
              {msg.content}
            </div>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-[#fbfaf7] via-[#fbfaf7] to-transparent pb-6 pt-10 px-4">
        <form onSubmit={handleSubmit} className="max-w-3xl mx-auto relative border border-[#e5e5e0] rounded-2xl bg-white shadow-sm focus-within:border-gray-400 transition">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSubmit(e); } }}
            placeholder="Ask about technical competencies..."
            className="w-full bg-transparent resize-none outline-none py-4 pl-4 pr-12 text-sm text-gray-900 max-h-32 h-14"
          />
          <button type="submit" disabled={isLoading} className="absolute right-3 bottom-3 p-1.5 rounded-lg bg-gray-900 text-white disabled:bg-gray-200 transition">
            ↑
          </button>
        </form>
      </div>
    </div>
  );
}