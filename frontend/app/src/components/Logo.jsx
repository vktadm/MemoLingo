import logoUrl from "./static/MemoLingo.svg?react";

function LogoSVG({ width = "100%", maxWidth = "150px", ...props }) {
  return (
    <img
      src={logoUrl}
      alt="MemoLingo Logo"
      style={{
        width: width,
        height: "auto",
        maxWidth: maxWidth,
        display: "block",
        marginLeft: "auto",
        marginRight: "auto",
      }}
      {...props}
    />
  );
}

export function Logo({ ...props }) {
  return (
    <div style={{ textAlign: "center" }}>
      <LogoSVG {...props} />
    </div>
  );
}
