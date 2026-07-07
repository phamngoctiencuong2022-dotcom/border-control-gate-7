export default function Modal({ title, children }) {
  return (
    <div className="modal-overlay fixed inset-0 bg-black/30 flex items-center justify-center p-4 z-50">
      <div className="modal w-full max-w-md rounded-xl bg-white border border-slate-200 shadow-xl overflow-hidden">
        <header className="modal-header border-b border-slate-200 px-5 py-4 bg-slate-50">
          <h3 className="text-lg font-semibold text-slate-900">{title}</h3>
        </header>
        <div className="modal-body p-5">{children}</div>
      </div>
    </div>
  );
}
