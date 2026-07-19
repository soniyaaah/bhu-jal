import { useState, useMemo } from "react";
import { Sidebar } from './Sidebar';

export const LayoutContainer = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="flex min-h-screen bg-[#111827]">
      <Sidebar />
      <main className="flex-1 ml-64 p-10 overflow-auto">
        {children}
      </main>
    </div>
  );
};
