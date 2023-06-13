/** @type {import('next').NextConfig} */
const nextConfig = {
  rewrites: async () => {
    return [
      {
        source: "/api/:path*",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.01:5050/api/:path*"
            : "/api/",
      },
    ];
  },
};

module.exports = nextConfig;
