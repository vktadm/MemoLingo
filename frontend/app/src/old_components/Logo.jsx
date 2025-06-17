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
        marginLeft: "auto",
        marginRight: "auto",
      }}
      {...props}
    />
  );
}

export function LogoCommon({ ...props }) {
  return (
    <div style={{ textAlign: "center" }}>
      <Logo {...props} />
    </div>
  );
}
