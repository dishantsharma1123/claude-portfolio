"use client";
import React from 'react';

interface SidebarProps {
  isOpen: boolean;
  setIsOpen: (open: boolean) => void;
}

export default function Sidebar({ isOpen, setIsOpen }: SidebarProps) {
  return (
    <div className={`fixed inset-y-0 left-0 z-40 w-64 bg-[#f3f2ee] border-r border-[#e5e5e0] transform ${isOpen ? "translate-x-0" : "-translate-x-full"} transition-transform duration-300 ease-in-out flex flex-col justify-between`}>
      <div className="p-4">
        <h2 className="text-sm font-semibold tracking-wider uppercase text-gray-500 mb-6">Dishant Sharma AI</h2>
        <nav className="space-y-2">
          {["About Me", "Experience", "Skills", "Projects", "Resume"].map((item) => (
            <button key={item} className="w-full text-left px-3 py-2 text-sm font-medium text-gray-700 rounded-md hover:bg-[#e8e7e3] transition">
              {item}
            </button>
          ))}
        </nav>
      </div>
      <div className="p-4 border-t border-[#e5e5e0] text-xs text-gray-400">
        © 2026 Dishant Sharma
      </div>
    </div>
  );
}