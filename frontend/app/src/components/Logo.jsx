import logoUrl from "./static/MemoLingo.svg?react";

function Logo({ ...props }) {
  return <img src={logoUrl} alt="Logo" props />;
}

export function LogoCommon() {
  return <Logo />;
}
