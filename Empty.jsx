export default function Empty({ message = "Không có dữ liệu" }) {
  return (
    <div className="empty text-center text-slate-500 py-8">
      <p>{message}</p>
    </div>
  );
}
