import { useState, useMemo } from "react";
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, RadioTower, BarChart3, LineChart, Map } from 'lucide-react';
import clsx from 'clsx';

export const Sidebar = () => {
  const navItems = [
    { name: 'Dashboard', path: '/', icon: LayoutDashboard },
    { name: 'Stations', path: '/stations', icon: RadioTower },
    { name: 'Forecast', path: '/forecast', icon: LineChart },
    { name: 'Analytics', path: '/analytics', icon: BarChart3 },
    { name: 'Maps', path: '/maps', icon: Map },
  ];

  return (
    <div className="w-64 h-screen bg-[#14151a] border-r border-gray-800 flex flex-col hidden md:flex fixed top-0 left-0">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-cyan-400">Bhu-Jal</h1>
        <p className="text-xs text-gray-500 font-semibold tracking-wider mt-1 uppercase">Precision Water Mgmt</p>
      </div>

      <nav className="flex-1 mt-6">
        <ul className="space-y-1">
          {navItems.map((item) => (
            <li key={item.path}>
              <NavLink
                to={item.path}
                className={({ isActive }) =>
                  clsx(
                    'flex items-center px-6 py-3 text-sm font-medium transition-colors',
                    isActive
                      ? 'text-cyan-400 bg-gray-800/50 border-r-2 border-cyan-400'
                      : 'text-gray-400 hover:text-gray-100 hover:bg-gray-800/30'
                  )
                }
              >
                <item.icon className="w-5 h-5 mr-4" />
                {item.name}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
      
      <div className="p-6">
        <div className="bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 rounded p-3 text-center cursor-pointer text-sm font-semibold hover:bg-cyan-500/20 transition-all">
          + Add Station
        </div>
      </div>
    </div>
  );
};
