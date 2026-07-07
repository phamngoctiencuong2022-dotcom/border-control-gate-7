export default function Input({ value, onChange, ...rest }) {
  return (
    <input
      className="w-full rounded-md border border-slate-300 px-3 py-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500"
      value={value}
      onChange={onChange}
      {...rest}
    />
  );
}
