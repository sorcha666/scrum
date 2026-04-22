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
    
    labels = [
        "US-01 Authenticate",
        "US-02 Create Library",
        "US-03 Hire Staff",
        "US-05 Assign Manager",
        "US-06 Unique Book IDs",
        "US-08 Register Author",
        "US-09 Register Publisher",
        "US-11 Write Book Summary",
        "US-12 Create Online Card",
        "US-13 Provide Purchase Advice"
    ]
    ys = evenly_spaced(11.5, 1.0, len(labels))
    ucs = [draw_usecase(ax, 8.7, y, lbl) for y, lbl in zip(ys, labels)]
    
    for lbl, uc in zip(labels, ucs):
        if "US-01" in lbl: draw_association(ax, u, uc)
        if "US-02" in lbl or "US-03" in lbl or "US-05" in lbl or "US-06" in lbl or "US-08" in lbl or "US-09" in lbl: draw_association(ax, sc, uc)
        if "US-11" in lbl or "US-13" in lbl: draw_association(ax, lp, uc)
        if "US-12" in lbl: draw_association(ax, h, uc)

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
    
    labels = [
        "US-14 Authorize Book",
        "US-20 Record Purchase",
        "US-22 Purchase by Edition",
        "US-23 Complete Stock",
        "US-24 Auto-Numbering",
        "US-25 Distribute Books",
        "US-29 Apply 3-Book Limit",
        "US-30 Late Return Fee",
        "US-34 Check Availability"
    ]
    ys = evenly_spaced(10.5, 0.8, len(labels))
    ucs = [draw_usecase(ax, 8.7, y, lbl) for y, lbl in zip(ys, labels)]
    
    for lbl, uc in zip(labels, ucs):
        if "US-14" in lbl or "US-20" in lbl or "US-22" in lbl or "US-23" in lbl or "US-24" in lbl or "US-25" in lbl: draw_association(ax, sc, uc)
        if "US-29" in lbl: draw_association(ax, sys, uc)
        if "US-30" in lbl: draw_association(ax, bib, uc)
        if "US-34" in lbl: draw_association(ax, lec, uc)

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
    
    labels = [
        "US-35 Online Reservation",
        "US-36 Auto-Cancel (48h)",
        "US-39 Create Transfer Slip",
        "US-04 Add New Services",
        "US-07 Register Pro Reader",
        "US-10 Publisher Status",
        "US-15 Assign Keywords",
        "US-16 Link Author/Genre",
        "US-18 Consult Editions",
        "US-19 Consult Prices",
        "US-21 Manage Defunct Publisher"
    ]
    ys = evenly_spaced(10.5, 0.8, len(labels))
    ucs = [draw_usecase(ax, 8.7, y, lbl) for y, lbl in zip(ys, labels)]
    
    for lbl, uc in zip(labels, ucs):
        if "US-35" in lbl: draw_association(ax, lec, uc)
        if "US-36" in lbl or "US-04" in lbl or "US-07" in lbl or "US-10" in lbl or "US-16" in lbl or "US-18" in lbl or "US-19" in lbl: draw_association(ax, sc, uc)
        if "US-39" in lbl or "US-21" in lbl: draw_association(ax, bib, uc)
        if "US-15" in lbl: draw_association(ax, lp, uc)

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
    
    labels = [
        "US-26 Manage Condition",
        "US-27 Renew Card",
        "US-28 Log Child Loan",
        "US-31 Repair Fees",
        "US-32 Record Conflicts",
        "US-33 Full Book History",
        "US-37 Loan Statistics",
        "US-38 Identify Stock Deficit",
        "US-17 Genre Commentary"
    ]
    ys = evenly_spaced(10.5, 0.8, len(labels))
    ucs = [draw_usecase(ax, 8.7, y, lbl) for y, lbl in zip(ys, labels)]
    
    for lbl, uc in zip(labels, ucs):
        if "US-26" in lbl or "US-31" in lbl or "US-32" in lbl or "US-33" in lbl or "US-38" in lbl: draw_association(ax, bib, uc)
        if "US-27" in lbl: draw_association(ax, lec, uc)
        if "US-28" in lbl or "US-37" in lbl: draw_association(ax, sc, uc)
        if "US-17" in lbl: draw_association(ax, lp, uc)

    plt.savefig(os.path.join(ASSETS_DIR, 'sprint4_usecase.png'), dpi=180, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    if not os.path.exists(ASSETS_DIR): os.makedirs(ASSETS_DIR)
    generate_sprint1()
    generate_sprint2()
    generate_sprint3()
    generate_sprint4()
    print("English UML Diagrams generated successfully in assets/ folder!")
