"""
UML Use Case Diagrams — English Version
Sprint 1: Authentication & Foundations (31 SP)
Sprint 2: Acquisitions & Loans (32 SP)
Sprint 3: Reservations & Catalogue (31 SP)
Sprint 4: Quality & Transfers (30 SP)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(OUTPUT_DIR, 'assets')
BLACK = '#000000'
WHITE = '#FFFFFF'
GREEN_ARROW = '#4CAF50'

def draw_actor(ax, x, y, label):
    # Head
    ax.add_patch(plt.Circle((x, y+0.75), 0.12, fill=False, edgecolor=BLACK, linewidth=1.2, zorder=5))
    # Body
    ax.plot([x,x],[y+0.63,y+0.32], color=BLACK, linewidth=1.2, zorder=5)
    # Arms
    ax.plot([x-0.18,x+0.18],[y+0.50,y+0.50], color=BLACK, linewidth=1.2, zorder=5)
    # Legs
    ax.plot([x,x-0.13],[y+0.32,y+0.07], color=BLACK, linewidth=1.2, zorder=5)
    ax.plot([x,x+0.13],[y+0.32,y+0.07], color=BLACK, linewidth=1.2, zorder=5)
    ax.text(x, y-0.1, label, ha='center', va='top', fontsize=8, color=BLACK, zorder=6, multialignment='center')
    return (x, y)

def draw_inheritance(ax, child_xy, parent_xy, route_y=13.0, x_offset=0, route_x_offset=0):
    cx, cy = child_xy[0], child_xy[1]
    px, py = parent_xy[0], parent_xy[1]
    vx = cx + route_x_offset
    ax.plot([cx, vx], [cy+0.9, cy+0.9], color=GREEN_ARROW, linewidth=1.2, zorder=2)
    ax.plot([vx, vx], [cy+0.9, route_y], color=GREEN_ARROW, linewidth=1.2, zorder=2)
    ax.plot([vx, px + x_offset], [route_y, route_y], color=GREEN_ARROW, linewidth=1.2, zorder=2)
    ax.plot([px + x_offset, px + x_offset], [route_y, py + 1.0], color=GREEN_ARROW, linewidth=1.2, zorder=2)
    
    # Triangle tip
    size = 0.25
    tip = [px + x_offset, py + 1.0]
    p1 = [tip[0] - size/2, tip[1] + size]
    p2 = [tip[0] + size/2, tip[1] + size]
    poly = patches.Polygon([tip, p1, p2], closed=True, fill=True, facecolor=WHITE, edgecolor=GREEN_ARROW, linewidth=1.2, zorder=3)
    ax.add_patch(poly)

def draw_usecase(ax, x, y, label, w=3.4, h=0.60):
    ax.add_patch(patches.Ellipse((x,y), w, h, fill=True, facecolor=WHITE, edgecolor=BLACK, linewidth=1.0, zorder=4))
    ax.text(x, y, label, ha='center', va='center', fontsize=6.5, color=BLACK, zorder=6)
    return (x, y)

def draw_association(ax, actor_xy, uc_pos):
    ax.plot([actor_xy[0], uc_pos[0]], [actor_xy[1]+0.45, uc_pos[1]], color=BLACK, linewidth=0.7, zorder=3)

def draw_system_boundary(ax, x, y, w, h, title):
    ax.add_patch(patches.Rectangle((x,y), w, h, fill=False, edgecolor=BLACK, linewidth=1.5, zorder=1))
    ax.text(x+w/2, y+h-0.35, title, ha='center', va='center', fontsize=10, fontweight='bold', color=BLACK, zorder=5)

def evenly_spaced(start_y, end_y, n):
    if n <= 1: return [(start_y + end_y) / 2]
    step = (start_y - end_y) / (n - 1)
    return [start_y - i * step for i in range(n)]

def generate_sprint1():
    fig, ax = plt.subplots(figsize=(18, 14))
    ax.set_xlim(-2, 18); ax.set_ylim(-1, 16.5); ax.set_aspect('equal'); ax.axis('off')
    fig.patch.set_facecolor(WHITE)
    
    ax.text(8.5, 16.2, "Use Case Diagram\nSprint 1 — Authentication & Foundations (31 SP)", ha='center', va='top', fontsize=12, fontweight='bold')
    draw_system_boundary(ax, 4, 0, 9.5, 13.0, 'Sprint 1: Foundations')
    
    u = draw_actor(ax, 1, 11.5, 'User')
    sc = draw_actor(ax, 0.5, 5.5, 'Central\nService')
    lp = draw_actor(ax, 16, 9.0, 'Pro\nReader')
    h = draw_actor(ax, 16, 4.0, 'Resident')
    
    draw_inheritance(ax, sc, u, route_y=13.5, x_offset=0.4, route_x_offset=-1.0)
    draw_inheritance(ax, lp, u, route_y=14.5, x_offset=0, route_x_offset=0.6)
    draw_inheritance(ax, h, u, route_y=15.2, x_offset=-0.4, route_x_offset=1.2)
    
    data = [
        ("Authenticate", "US-01"),
        ("Create Library", "US-02"),
        ("Hire Staff", "US-03"),
        ("Assign Manager", "US-05"),
        ("Unique Book IDs", "US-06"),
        ("Register Author", "US-08"),
        ("Register Publisher", "US-09"),
        ("Write Book Summary", "US-11"),
        ("Create Online Card", "US-12"),
        ("Provide Purchase Advice", "US-13")
    ]
    ys = evenly_spaced(11.5, 1.0, len(data))
    ucs = [draw_usecase(ax, 8.7, y, d[0]) for y, d in zip(ys, data)]
    
    for (lbl, us_id), uc in zip(data, ucs):
        if us_id == "US-01": draw_association(ax, u, uc)
        if us_id in ["US-02", "US-03", "US-05", "US-06", "US-08", "US-09"]: draw_association(ax, sc, uc)
        if us_id in ["US-11", "US-13"]: draw_association(ax, lp, uc)
        if us_id == "US-12": draw_association(ax, h, uc)

    plt.savefig(os.path.join(ASSETS_DIR, 'sprint1_usecase.png'), dpi=180, bbox_inches='tight')
    plt.close()

def generate_sprint2():
    fig, ax = plt.subplots(figsize=(18, 14))
    ax.set_xlim(-2, 18); ax.set_ylim(-1, 14); ax.set_aspect('equal'); ax.axis('off')
    fig.patch.set_facecolor(WHITE)
    
    ax.text(8.5, 13.5, "Use Case Diagram\nSprint 2 — Acquisitions & Loans (32 SP)", ha='center', va='top', fontsize=12, fontweight='bold')
    draw_system_boundary(ax, 4, 0, 9.5, 12, 'Sprint 2: Acquisitions & Loans')
    
    sc = draw_actor(ax, 1, 8.0, 'Central\nService')
    bib = draw_actor(ax, 1, 2.0, 'Librarian')
    sys = draw_actor(ax, 16, 6.0, 'System')
    lec = draw_actor(ax, 16, 10.0, 'Reader')
    
    data = [
        ("Authorize Book", "US-14"),
        ("Record Purchase", "US-20"),
        ("Purchase by Edition", "US-22"),
        ("Complete Stock", "US-23"),
        ("Auto-Numbering", "US-24"),
        ("Distribute Books", "US-25"),
        ("Apply 3-Book Limit", "US-29"),
        ("Late Return Fee", "US-30"),
        ("Check Availability", "US-34")
    ]
    ys = evenly_spaced(10.5, 0.8, len(data))
    ucs = [draw_usecase(ax, 8.7, y, d[0]) for y, d in zip(ys, data)]
    
    for (lbl, us_id), uc in zip(data, ucs):
        if us_id in ["US-14", "US-20", "US-22", "US-23", "US-24", "US-25"]: draw_association(ax, sc, uc)
        if us_id == "US-29": draw_association(ax, sys, uc)
        if us_id == "US-30": draw_association(ax, bib, uc)
        if us_id == "US-34": draw_association(ax, lec, uc)

    plt.savefig(os.path.join(ASSETS_DIR, 'sprint2_usecase.png'), dpi=180, bbox_inches='tight')
    plt.close()

def generate_sprint3():
    fig, ax = plt.subplots(figsize=(18, 14))
    ax.set_xlim(-2, 18); ax.set_ylim(-1, 14); ax.set_aspect('equal'); ax.axis('off')
    fig.patch.set_facecolor(WHITE)
    
    ax.text(8.5, 13.5, "Use Case Diagram\nSprint 3 — Reservations & Catalogue (31 SP)", ha='center', va='top', fontsize=12, fontweight='bold')
    draw_system_boundary(ax, 4, 0, 9.5, 12, 'Sprint 3: Reservations & Catalogue')
    
    sc = draw_actor(ax, 1, 9.0, 'Central\nService')
    bib = draw_actor(ax, 1, 3.0, 'Librarian')
    lp = draw_actor(ax, 16, 9.0, 'Pro\nReader')
    lec = draw_actor(ax, 16, 4.0, 'Reader')
    
    data = [
        ("Online Reservation", "US-35"),
        ("Auto-Cancel (48h)", "US-36"),
        ("Create Transfer Slip", "US-39"),
        ("Add New Services", "US-04"),
        ("Register Pro Reader", "US-07"),
        ("Publisher Status", "US-10"),
        ("Assign Keywords", "US-15"),
        ("Link Author/Genre", "US-16"),
        ("Consult Editions", "US-18"),
        ("Consult Prices", "US-19"),
        ("Manage Defunct Publisher", "US-21")
    ]
    ys = evenly_spaced(10.5, 0.8, len(data))
    ucs = [draw_usecase(ax, 8.7, y, d[0]) for y, d in zip(ys, data)]
    
    for (lbl, us_id), uc in zip(data, ucs):
        if us_id == "US-35": draw_association(ax, lec, uc)
        if us_id in ["US-36", "US-04", "US-07", "US-10", "US-16", "US-18", "US-19"]: draw_association(ax, sc, uc)
        if us_id in ["US-39", "US-21"]: draw_association(ax, bib, uc)
        if us_id == "US-15": draw_association(ax, lp, uc)

    plt.savefig(os.path.join(ASSETS_DIR, 'sprint3_usecase.png'), dpi=180, bbox_inches='tight')
    plt.close()

def generate_sprint4():
    fig, ax = plt.subplots(figsize=(18, 14))
    ax.set_xlim(-2, 18); ax.set_ylim(-1, 14); ax.set_aspect('equal'); ax.axis('off')
    fig.patch.set_facecolor(WHITE)
    
    ax.text(8.5, 13.5, "Use Case Diagram\nSprint 4 — Quality & Transfers (30 SP)", ha='center', va='top', fontsize=12, fontweight='bold')
    draw_system_boundary(ax, 4, 0, 9.5, 12, 'Sprint 4: Quality & Transfers')
    
    sc = draw_actor(ax, 1, 9.0, 'Central\nService')
    bib = draw_actor(ax, 1, 3.0, 'Librarian')
    lp = draw_actor(ax, 16, 10.0, 'Pro\nReader')
    lec = draw_actor(ax, 16, 6.0, 'Reader')
    
    data = [
        ("Manage Condition", "US-26"),
        ("Renew Card", "US-27"),
        ("Log Child Loan", "US-28"),
        ("Repair Fees", "US-31"),
        ("Record Conflicts", "US-32"),
        ("Full Book History", "US-33"),
        ("Loan Statistics", "US-37"),
        ("Identify Stock Deficit", "US-38"),
        ("Genre Commentary", "US-17")
    ]
    ys = evenly_spaced(10.5, 0.8, len(data))
    ucs = [draw_usecase(ax, 8.7, y, d[0]) for y, d in zip(ys, data)]
    
    for (lbl, us_id), uc in zip(data, ucs):
        if us_id in ["US-26", "US-31", "US-32", "US-33", "US-38"]: draw_association(ax, bib, uc)
        if us_id == "US-27": draw_association(ax, lec, uc)
        if us_id in ["US-28", "US-37"]: draw_association(ax, sc, uc)
        if us_id == "US-17": draw_association(ax, lp, uc)

    plt.savefig(os.path.join(ASSETS_DIR, 'sprint4_usecase.png'), dpi=180, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    if not os.path.exists(ASSETS_DIR): os.makedirs(ASSETS_DIR)
    generate_sprint1()
    generate_sprint2()
    generate_sprint3()
    generate_sprint4()
    print("English UML Diagrams generated successfully in assets/ folder!")
