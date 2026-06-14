import './globals.css';

export const metadata = {
  title: 'Dishant Sharma | AI Portfolio',
  description: 'AI-Integrated Full-Stack Engineer Portfolio',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}