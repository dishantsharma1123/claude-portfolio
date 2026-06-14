"use client";
import React, { useState } from 'react';
import Sidebar from '@/components/Sidebar';
import ChatInterface from '@/components/ChatInterface';

export default function Home() {
  const [sidebarOpen, setSidebarOpen] = useState(true);

  return (
    <div className="h-screen flex bg-[#fbfaf7] overflow-hidden relative">
      <Sidebar isOpen={sidebarOpen} setIsOpen={setSidebarOpen} />
      <main className={`flex-1 flex flex-col h-full transition-all duration-300 ${sidebarOpen ? 'ml-64' : 'ml-0'}`}>
        <header className="h-14 border-b border-[#e5e5e0] flex items-center px-6 justify-between bg-[#fbfaf7]/80 backdrop-blur-md z-10">
          <button onClick={() => setSidebarOpen(!sidebarOpen)} className="text-gray-500 hover:text-black transition">
            ☰
          </button>
          <div className="text-xs font-semibold uppercase tracking-wider text-gray-400">Claude Core 3.5 Engine Replication</div>
        </header>
        <div className="flex-1 overflow-hidden relative">
           <ChatInterface />
        </div>
      </main>
    </div>
  );
}