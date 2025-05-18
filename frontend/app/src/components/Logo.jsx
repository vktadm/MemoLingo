import logoUrl from "./static/MemoLingo.svg?react";

function Logo({ width = "100%", maxWidth = "150px", ...props }) {
  return (
    <img
      src={logoUrl}
      alt="MemoLingo Logo"
      style={{
        width: width,
        height: "auto",
        maxWidth: maxWidth,
        display: "block",
      }}
      {...props}
    />
  );
}

export function LogoCommon() {
  return <Logo className="img-fluid" />;
}
