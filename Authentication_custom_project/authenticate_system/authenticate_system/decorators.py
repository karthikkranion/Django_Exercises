from django.contrib.auth.decorators import login_required # type: ignore
from functools import wraps
from django.http import HttpResponseForbidden  #type:ignore

error_page='''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Error Loading</title>
  <style>
    :root{
      --bg:#0f1724;       /* deep navy */
      --card:#0b1220;     /* darker card */
      --muted:#9aa4b2;
      --accent:#60a5fa;   /* soft blue */
      --glass: rgba(255,255,255,0.04);
      --radius:20px;
      --shadow: 0 8px 30px rgba(2,6,23,0.6);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%;margin:0;background:linear-gradient(180deg,var(--bg),#071023 80%);color:#e6eef8}
    .wrap{min-height:100%;display:flex;align-items:center;justify-content:center;padding:40px}
    .card{
      width:100%;max-width:820px;background:linear-gradient(180deg,var(--card),rgba(11,18,32,0.85));
      border-radius:var(--radius);box-shadow:var(--shadow);backdrop-filter: blur(6px);
      padding:40px;display:grid;grid-template-columns: 140px 1fr;gap:28px;align-items:center;
      border: 1px solid rgba(255,255,255,0.03);
    }
    .badge{
      height:120px;width:120px;border-radius:18px;display:flex;align-items:center;justify-content:center;
      background:linear-gradient(135deg,var(--accent),#7dd3fc);color:#042135;font-weight:700;font-size:34px;
      box-shadow: 0 6px 20px rgba(96,165,250,0.12);
    }
    .content h1{font-size:34px;margin:0 0 8px 0;letter-spacing:-0.4px}
    .code{display:inline-block;padding:6px 10px;border-radius:8px;background:var(--glass);color:var(--accent);
         font-weight:700;margin-right:10px;font-family:monospace}
    .desc{color:var(--muted);line-height:1.6;margin-bottom:18px}
    .actions{display:flex;gap:12px;flex-wrap:wrap}
    .btn{
      display:inline-block;padding:10px 16px;border-radius:12px;text-decoration:none;font-weight:600;
      border:1px solid rgba(255,255,255,0.04);
      background:linear-gradient(180deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));
      color:#eaf6ff;
      box-shadow: 0 4px 18px rgba(2,6,23,0.45);
    }
    .btn-primary{background:linear-gradient(180deg,var(--accent),#3b82f6);color:#042135;border:none}
    .hint{font-size:13px;color:var(--muted);margin-top:8px}
    @media (max-width:640px){
      .card{grid-template-columns:1fr; text-align:center}
      .badge{margin:0 auto}
      .content h1{font-size:28px}
    }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card" role="main" aria-labelledby="title">
      <div class="badge" aria-hidden="true">Error</div>

      <div class="content">
        <div style="display:flex;align-items:baseline;gap:8px;flex-wrap:wrap">
          <span class="code">Error</span>
          <h1 id="title">403 Forbidden </h1>
        </div>

        <p class="desc">You are not authorised to view this page</p>

        <div class="actions">
          <a href="/" class="btn btn-primary">Return to Home</a>
          <a href='#' class="btn">Contact support</a>
        </div>

        <div class="hint">Tip: you can also try <strong>clearing cache</strong> or check the URL for typos.</div>
      </div>
    </div>
  </div>
</body>
</html>
'''

def login_and_user_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapper(request,*args,**kwargs):
            user=request.user
            if required_role == 'customer' and not user.is_customer:
                return HttpResponseForbidden(error_page)
            if required_role == 'seller' and not user.is_seller:
                return HttpResponseForbidden(error_page)
            return view_func(request,*args,**kwargs)
        return _wrapper
    return decorator

