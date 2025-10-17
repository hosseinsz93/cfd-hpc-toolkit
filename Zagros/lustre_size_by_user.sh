# Set the base; script will auto-detect which exists
BASE=/mnt/lustre
[ -d /mnt/lustre/users ] && BASE=/mnt/lustre/users

printf "%-24s %12s\n" "user" "size"
echo "----------------------------------------------"
for d in "$BASE"/*; do
  [ -d "$d" ] || continue
  u=$(basename "$d")
  # bytes (accurate for sorting), then pretty
  bytes=$(du -sb "$d" 2>/dev/null | cut -f1)
  human=$(numfmt --to=iec --suffix=B "$bytes")
  printf "%-24s %12s\n" "$u" "$human"
done | sort -hk2

